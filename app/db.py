from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Base


# Database URL
DATABASE_URL = "sqlite:///data/twende.db"

# Seting up SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Creating a configured "Session" class to interact with the Database
Session = sessionmaker(bind=engine)

# initializes the data
def init_db():
    import models
    # Function to create tables
    Base.metadata.create_all(bind=engine)
