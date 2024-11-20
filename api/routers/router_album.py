from fastapi import APIRouter, status, Depends, Request , HTTPException
from services import albums
from sqlalchemy.orm import Session
from schema.schema import AlbumCreate,Album,User
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
        albums_data = albums.get_albums(10, db)  # Example: 10 albums by default
    
    if albums_data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No albums found")
    
    print(f"Albums data: {albums_data}")  # Debugging output
    
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
    # Utiliser le paramètre 'q' pour obtenir l'album spécifique
    albums_data = albums.get_album_by_id(q, db)
    
    # Retourner la page catalogue avec les données de l'album correspondant à 'q'
    return templates.TemplateResponse("catalogue.html", {"request": request, "albums": [albums_data]})



# @router.post("/catalogue")
# async def create_album(album : AlbumCreate = Depends(), db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
#     return albums.create_album(album,db)

# @router.get("/catalogue")
# async def get_album_by_name(album_name: str,db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
#     return albums.get_album_by_name(album_name= album_name, db = db)


# @router.get("/catalogue")
# async def get_album_by_id(album_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
#     return albums.get_album_by_id(id = album_id, db =db)

# @router.get("/catalogue")
# async def get_albums_by_artist(artist_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
#     return albums.get_album_by_id(id = artist_id, db =db)

# @router.get("/catalogue")
# async def get_albums(num_album :int, db: Session  = Depends(get_db), current_user: User = Depends(get_current_user)):
#     return albums.get_albums(num_album=num_album, db=db)

# @router.get("/albums")
# async def get_albums_with_minimum_sales(threshold: int,db: Session  = Depends(get_db), current_user: User = Depends(get_current_user)):
#     return albums.get_albums_with_minimum_sales(threshold= threshold, db= db)

# @router.delete("/{id}")
# async def delete_albums(album_id :int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
#     return albums.delete_album(album_id= album_id, db = db)

