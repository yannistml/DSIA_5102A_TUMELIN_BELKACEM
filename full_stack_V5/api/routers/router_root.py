from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
import os
from models.database import BaseSQL, engine
from services.register import register_user
from schema.schema import User, UserCreate
from sqlalchemy.orm import Session
from models.database import get_db


router = APIRouter()

@router.on_event("startup")
async def startup_event():
    print(os.listdir())
    BaseSQL.metadata.create_all(bind=engine)
