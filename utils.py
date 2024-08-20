# utils.py - Contains utility functions for the application

import os
import openai
from sqlalchemy import Table, Column, String, Boolean, MetaData

openai.api_key = os.getenv("OPENAI_API_KEY")

def is_technology_company(description):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Is the following company a technology company? Description: {description}",
        max_tokens=5,
        n=1,
        stop=None,
        temperature=0
    )
    answer = response.choices[0].text.strip().lower()
    return "yes" in answer

def create_table_in_db(df, engine):
    metadata = MetaData(bind=engine)
    columns = []
    for column_name, dtype in zip(df.columns, df.dtypes):
        if dtype == 'object':
            columns.append(Column(column_name, String))
        elif dtype == 'bool':
            columns.append(Column(column_name, Boolean))
        else:
            columns.append(Column(column_name, String))  # Defaulting other types to String
    
    table = Table('companies', metadata, *columns)
    metadata.create_all(engine)
