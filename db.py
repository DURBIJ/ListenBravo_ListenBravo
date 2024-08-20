# db.py - Handles database connection and setup

from sqlalchemy import create_engine, MetaData

DATABASE_URL = "postgresql://durbijSQL:durbijroot@localhost:5432/mydatabase" 

engine = create_engine(DATABASE_URL)
metadata = MetaData()

def get_db_engine():
    return engine
