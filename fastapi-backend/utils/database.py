"""
Database configuration and models.
"""

from sqlalchemy import create_engine, Column, Integer, String, Time, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from data.mock_data import MOCK_OUTLETS

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

SQLALCHEMY_DATABASE_URL = "sqlite:///./data/zus.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Outlet(Base):
    __tablename__ = "outlets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    opening_time = Column(String)
    closing_time = Column(String)

# Create tables and populate with mock data
def init_db():
    Base.metadata.create_all(bind=engine)
    
    # Add mock data
    db = SessionLocal()
    try:
        # Check if we already have data
        if db.query(Outlet).first() is None:
            for outlet_data in MOCK_OUTLETS:
                outlet = Outlet(**outlet_data)
                db.add(outlet)
            db.commit()
    finally:
        db.close()

# Initialize database with mock data
init_db()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 