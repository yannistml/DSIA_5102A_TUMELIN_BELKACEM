
from sqlalchemy import Column, Integer, String,  Float, ForeignKey 
from .database import BaseSQL

class AlbumDB(BaseSQL):
    __tablename__ = "albums"
    unique_id = Column(Integer, primary_key=True, index=True)
    artist_id = Column(Integer, nullable=False)
    album_title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    year_of_pub = Column(Integer, nullable=False)
    num_of_tracks = Column(Integer, nullable=False)
    num_of_sales = Column(Integer, nullable=False)
    rolling_stone_critic = Column(Float, nullable=False)
    mtv_critic = Column(Float, nullable=False)
    music_maniac_critic = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))


class UserDB(BaseSQL):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    token = Column(String)