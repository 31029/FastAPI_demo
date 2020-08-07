from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:hzy991220@host.docker.internal:3306/hzy?charset=utf8mb4"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    pool_pre_ping=True,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()