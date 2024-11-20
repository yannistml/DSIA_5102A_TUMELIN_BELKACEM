from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from models.post import AlbumDB
from typing import List
from schema import schema


def get_album_by_id(id: int, db: Session): 
    album = db.query(AlbumDB).filter(AlbumDB.unique_id == id ).first()
    if not album:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="album not found in the table")
    return album

def get_album_by_name(album_name: str, db: Session): 
    album = db.query(AlbumDB).filter(AlbumDB.album_title == album_name ).first()
    if not album:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="album not found in the table")
    return album


def get_albums_by_artist(artist_id: int, db: Session) :
    albums = db.query(AlbumDB.album_db).filter(AlbumDB.artist_id == artist_id).all()
    if not albums:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="artits is not found in the table")
    return albums 


def create_album(request: schema.AlbumCreate, db:  Session):
    album = db.query(AlbumDB).filter(AlbumDB.album_title == request.album_title, AlbumDB.artist_id == request.artist_id).first()
    if album : 
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Album already exists in the catalogue")

def get_albums(num_album :int,db: Session):
    albums = db.query(AlbumDB).filter().limit(num_album).all()

def delete_album(album_id: int, db: Session):
    album = db.query(AlbumDB).filter(AlbumDB.unique_id == album_id).first()
    
    if not album:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Album not found"
        )
    
    # Delete the album
    db.delete(album)
    db.commit()

def get_albums_with_minimum_sales(threshold: int, db : Session):
    albums = db.query(AlbumDB).filter(AlbumDB.num_of_sales > threshold).all()
    if not albums :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"There are no albums with more than {threshold} sales"
        )
    return albums