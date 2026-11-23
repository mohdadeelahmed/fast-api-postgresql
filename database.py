import os
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_engine("postgresql://postgres:password@localhost/item_db", echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)