import pandas as pd
from models import post
from sqlalchemy import text

from models.database import SessionLocal, engine, BaseSQL

albums_df = pd.read_csv("albums.csv")
session = SessionLocal()

def insert_albums(albums_df,session):
    existing_album_count = session.query(post.AlbumDB).count()

    if existing_album_count > 0:
        print("Albums are already in the database. Skipping insert.")
        return
    for _,row in albums_df.iterrows():
        try :
            session.execute(
                text(
                """
                INSERT INTO albums (unique_id, artist_id, album_title, genre, year_of_pub, num_of_tracks, num_of_sales, rolling_stone_critic, mtv_critic, music_maniac_critic)
                VALUES (:unique_id, :artist_id, :album_title, :genre, :year_of_pub, :num_of_tracks, :num_of_sales, :rolling_stone_critic, :mtv_critic, :music_maniac_critic)
                ON CONFLICT (unique_id) DO NOTHING
                """
                ),
                {
                    "unique_id": row["id"],
                    "artist_id": row["artist_id"],
                    "album_title": row["album_title"],
                    "genre": row["genre"],
                    "year_of_pub": row["year_of_pub"],
                    "num_of_tracks": row["num_of_tracks"],
                    "num_of_sales": row["num_of_sales"],
                    "rolling_stone_critic": row["rolling_stone_critic"],
                    "mtv_critic": row["mtv_critic"],
                    "music_maniac_critic": row["music_maniac_critic"],
                },
            )
            session.commit()
            print(f"Inserted album with unique_id: {row['id']}")

        except Exception as e:
            print(f"Error inserting album with unique_id {row['id']}: {e}")
            session.rollback()