from fastapi import APIRouter
from models.database import BaseSQL, engine, SessionLocal
from create_db import insert_albums
import pandas as pd

router = APIRouter()


@router.on_event("startup")
async def initialize_db():
    try:
        # Create tables
        print("Initializing database...")
        BaseSQL.metadata.create_all(bind=engine)
        print("Tables created successfully.")

        # Load data
        albums_df = pd.read_csv("albums.csv")
        print(f"CSV loaded: {albums_df.head()}")
        session = SessionLocal()
        insert_albums(albums_df, session)
        print("Albums inserted successfully.")
    except Exception as e:
        print(f"Database initialization error: {e}")
