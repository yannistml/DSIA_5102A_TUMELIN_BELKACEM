from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers import router_user,router_album,router_root

from models.database import BaseSQL, engine


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.state.templates = templates

app.include_router(router_root.router)
app.include_router(router_user.router)
app.include_router(router_album.router)