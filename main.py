from pathlib import Path

from fastapi import FastAPI, Depends, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
# from typing import List

from src.database.db import get_db
from src.routes import contacts, auth


app = FastAPI()

app.include_router(contacts.router)
app.include_router(contacts.search_router)
app.include_router(auth.auth_router)

@app.get("/")
def read_root():
    return {"message": "Your contacts here"}

@app.get("/api/healthchecker")
async def healthchecker(db: AsyncSession = Depends(get_db)):
    try:
        # Make request
        result = await db.execute(text("SELECT 1"))
        result = result.fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail="Database is not configured correctly")
        return {"message": "Database 'contacts' is healthy"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connecting to the database")