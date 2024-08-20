# main.py - Entry point of the FastAPI application

from fastapi import FastAPI, File, UploadFile, HTTPException
import pandas as pd
from io import StringIO
from utils import is_technology_company, create_table_in_db
from db import get_db_engine

app = FastAPI()

@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="File format not supported. Please upload a CSV file.")
    
    content = await file.read()
    df = pd.read_csv(StringIO(content.decode("utf-8")))

    if "Description" not in df.columns:
        raise HTTPException(status_code=400, detail="CSV does not contain 'Description' column.")

    # Step 3: Create "Technology Company" column using LLM
    df['Technology Company'] = df['Description'].apply(is_technology_company)

    # Step 4: Create a new table in the database
    create_table_in_db(df, get_db_engine())

    return {"message": "CSV processed successfully and table created in the database"}
