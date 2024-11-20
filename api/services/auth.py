from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from typing import Optional
from schema.schema import TokenData, User
from passlib.context import CryptContext
from fastapi import Response,Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from models import post 
import hashlib
from models.database import get_db 
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse

SECRET_KEY = "YOUR_SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now()+ timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_Token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usrname: str = payload.get("sub")
        if usrname is None:
            raise credentials_exception
        return TokenData(username=usrname)
    except (JWTError):
        raise credentials_exception

#Hash
#class Hash():
#    def bcrypt(password:str):
#        return pwd_context.hash(password)
    
#    def verify(hash_password, plain_password):
#        return pwd_context.verify(plain_password, hash_password)
    

def get_user(db: Session, username: str):
    return db.query(post.UserDB).filter(post.UserDB.username == username).first()

async def get_current_user(request : Request, db: Session = Depends(get_db)):

    token = request.headers.get("cookie", "")[6:]

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if token :

        token_data = verify_Token(token,credentials_exception)
    else :
        raise credentials_exception

    user = get_user(db, username=token_data.username)

    if user is None:
        raise credentials_exception
    return user


def login(authentified :str,request:OAuth2PasswordRequestForm,db: Session):
    if authentified:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="There is already an active session",
        )
    user = db.query(post.UserDB).filter(post.UserDB.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Username not found")
    
    if user.hashed_password!= str(hashlib.sha256(request.password.encode()).hexdigest()):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid password for this username")

    token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": str(request.username)}, expires_delta=token_expires)
    response = RedirectResponse(url="/catalogue", status_code=303)
    response.set_cookie(key="token", value=access_token, expires=token_expires, secure=True, httponly=True)

    return response

def logout(authentified :str, response: Response):
    if not authentified:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No active session",
        )
    response.delete_cookie(key="token")
    return {"message": "Cookie deleted"}
