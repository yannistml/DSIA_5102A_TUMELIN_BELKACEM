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
from services.auth import login, logout

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
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
    request: Request = None,
):
    hashed = str(hashlib.sha256(password.encode()).hexdigest())
    user = UserCreate(username=username, password=hashed)

    error_message = register_user(request=user, db=db)
    if error_message:
        templates = request.app.state.templates
        return templates.TemplateResponse(
            "register.html", {"request": request, "error_message": error_message}
        )

    return RedirectResponse(url="/login", status_code=303)


@router.get("/login")
async def login_page(request: Request):
    templates = request.app.state.templates
    return templates.TemplateResponse(name="login.html", request=request)


@router.post("/login")
async def login_page(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
    authentified: Annotated[str, Cookie()] = None,
):
    return login(authentified=authentified, request=request, db=db)


@router.post("/logout")
async def logout(response: Response, authentified: Annotated[str, Cookie()] = None):
    return logout(authentified=authentified, response=response)
