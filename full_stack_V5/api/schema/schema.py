from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str
    token : Optional[str] = None

class User(BaseModel):
    username: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str

class Album(BaseModel):
    unique_id: Optional[int]
    artist_id: int
    album_title: str
    genre: str
    year_of_pub: int
    num_of_tracks: int
    num_of_sales: int
    rolling_stone_critic: float
    mtv_critic: float
    music_maniac_critic: float

class AlbumCreate(BaseModel):
    
    artist_id: int
    album_title: str
    genre: str
    year_of_pub: int
    num_of_tracks: int
    num_of_sales: int
    rolling_stone_critic: float
    mtv_critic: float
    music_maniac_critic: float

class UserInDB(User):
    hashed_password: str