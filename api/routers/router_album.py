from fastapi import APIRouter, status, Depends, Request , HTTPException
from services import albums
from sqlalchemy.orm import Session
from schema.schema import AlbumCreate,User
from  models.database import get_db
from services.auth import get_current_user
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/catalogue", response_class=HTMLResponse)
async def get_catalogue_page(request: Request, db: Session = Depends(get_db), album_name: str = None, album_id: int = None, num_album: int = None,sales : int = None, current_user: User = Depends(get_current_user)):
    # Handle fetching albums based on query parameters
    if album_name:
        albums_data = albums.get_album_by_name(album_name, db)
    elif album_id:
        albums_data = albums.get_album_by_id(album_id, db)
    elif num_album:
        albums_data = albums.get_albums(num_album, db)
    elif sales:
        albums_data = albums.get_albums_with_minimum_sales(sales, db)
    else:
        # If no specific query params are provided, fetch a default set of albums
        albums_data = albums.get_albums(10, db)  
    
    if albums_data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No albums found")
    
    
    return templates.TemplateResponse("catalogue.html", {"request": request, "albums": albums_data})

@router.post("/catalogue")
async def create_album(album : AlbumCreate = Depends(), db: Session = Depends(get_db)):
    return albums.create_album(album,db)

@router.post("/catalogue/{album_id}/delete")
async def delete_album(request: Request, album_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    
    albums.delete_album(album_id, db)

    albums_data = albums.get_albums(10, db)
    
    return templates.TemplateResponse("catalogue.html", {"request": request, "albums": albums_data})

@router.get("/catalogue/search/id")
async def search_album_by_id(request: Request, q: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # use parameter q to get the specific album
    albums_data = albums.get_album_by_id(q, db)
    
    return templates.TemplateResponse("catalogue.html", {"request": request, "albums": [albums_data]})





