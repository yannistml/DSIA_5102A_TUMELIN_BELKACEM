import pandas as pd
from api.models import post

from api.models.database import SessionLocal, engine, BaseSQL

albums_df = pd.read_csv("albums.csv")
session = SessionLocal()

def insert_albums(albums_df,session):
    for _,row in albums_df.itterrows():
        album = post.AlbumDB(
            unique_id = row["id"],
            artist_id = row["artist_id"],
            album_title = row["album_title"],
            genre = row["genre"],
            year_of_pub = row["year_of_pub"],
            num_of_tracks = row["num_of_tracks"],
            num_of_sales = row["num_of_sales"],
            rolling_stone_critic = row["rolling_stone_critic"],
            mtv_critic = row["mtv_critic"],
            music_maniac_critic = row["music_maniac_critic"],
        )
        session.add(album)
        session.commit()

try:
    BaseSQL.metadata.create_all(bind=engine)
    insert_albums(albums_df,session)
except Exception as e:
    print("datas are already in the database")