import hashlib
from fastapi import APIRouter, Depends, Request, Form, Response, Cookie
from sqlalchemy.orm import Session
from models.database import get_db
from schema.schema import UserCreate
from services.register import register_user
from fastapi.responses import HTMLResponse, RedirectResponse

from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from sqlalchemy.orm import Session
from services.auth import login,logout

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    templates = request.app.state.templates
    return templates.TemplateResponse(name="index.html", request=request)

@router.get("/register", response_class=HTMLResponse)
async def get_register_form(request: Request):
    templates = request.app.state.templates
    return templates.TemplateResponse(name="register.html", request=request)

@router.post("/register")
async def create_user(
    username: str = Form(...),            # Extract 'username' from the form
    password: str = Form(...),            # Extract 'password' from the form
    db: Session = Depends(get_db)
): 
    hashed = str(hashlib.sha256(password.encode()).hexdigest())
    user = UserCreate(username=username, password=hashed)

    register_user(request = user,db = db)
    return RedirectResponse(url="/login", status_code=303)

@router.get("/login")
async def login_page(request: Request):
    templates = request.app.state.templates
    return templates.TemplateResponse(name="login.html", request=request)


@router.post("/login")
async def login_page(request : OAuth2PasswordRequestForm= Depends(),db : Session = Depends(get_db),authentified: Annotated[str, Cookie()] = None):
    return login(authentified=authentified, request= request, db = db)


@router.post("/logout")
async def logout(response : Response,authentified: Annotated[str, Cookie()] = None):
    return logout(authentified= authentified, response= response)
    
# @router.post("/register")
# async def create_user( request : UserCreate = Depends(), db: Session= Depends(get_db)):
#     user = UserCreate(username=username, password=password)

#     return register_user(request = request,db = db)

# @router.get("/register")
# async def get_current_user(current_user : User = Depends(get_current_user)):
#     return current_user