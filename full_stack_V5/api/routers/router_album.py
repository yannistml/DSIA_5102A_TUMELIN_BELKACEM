from fastapi import APIRouter, status, Depends, Request
from services import albums
from sqlalchemy.orm import Session
from schema.schema import AlbumCreate,Album,User
from  models.database import get_db
from services.auth import get_current_user
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.post("/catalogue")
async def create_album(album : AlbumCreate = Depends(), db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return albums.create_album(album,db)

@router.get("/catalogue")
async def get_album_by_name(album_name: str,db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return albums.get_album_by_name(album_name= album_name, db = db)


@router.get("/catalogue")
async def get_album_by_id(album_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return albums.get_album_by_id(id = album_id, db =db)

@router.get("/catalogue")
async def get_albums_by_artist(artist_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return albums.get_album_by_id(id = artist_id, db =db)

@router.get("/catalogue")
async def get_albums(num_album :int, db: Session  = Depends(get_db), current_user: User = Depends(get_current_user)):
    return albums.get_albums(num_album=num_album, db=db)

@router.get("/albums")
async def get_albums_with_minimum_sales(threshold: int,db: Session  = Depends(get_db), current_user: User = Depends(get_current_user)):
    return albums.get_albums_with_minimum_sales(threshold= threshold, db= db)

@router.delete("/{id}")
async def delete_albums(album_id :int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return albums.delete_album(album_id= album_id, db = db)

