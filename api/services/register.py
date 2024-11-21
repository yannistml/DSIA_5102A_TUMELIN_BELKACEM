from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import post
from schema.schema import UserCreate

# from services.auth import Hash


def register_user(request: UserCreate, db: Session):

    record = (
        db.query(post.UserDB).filter(post.UserDB.username == request.username).first()
    )
    if record:
        return "This username is already taken"

    new_user = post.UserDB(
        username=request.username, hashed_password=request.password
    )  # Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return None
