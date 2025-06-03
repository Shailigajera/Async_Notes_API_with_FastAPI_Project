# from fastapi import FastAPI, HTTPException
# from . database import SessionLocal, engine
# from sqlalchemy.orm import Session
# from . import crud 
# from typing import List 


# models.Base.metadata.create_all(engine)


# @app.get()

from fastapi import FastAPI, HTTPException
from . import models, schemas, crud
from .database import database, metadata, engine

# Create tables
metadata.create_all(bind=engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/notes/", response_model=schemas.Note)
async def create_note(note: schemas.NoteCreate):
    return await crud.create_note(database, note)

@app.get("/notes/", response_model=list[schemas.Note])
async def read_notes():
    return await crud.get_notes(database)

@app.get("/notes/{note_id}", response_model=schemas.Note)
async def read_note(note_id: int):
    note = await crud.get_note(database, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@app.put("/notes/{note_id}", response_model=schemas.Note)
async def update_note(note_id: int, updated_note: schemas.NoteUpdate):
    existing = await crud.get_note(database, note_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Note not found")
    return await crud.update_note(database, note_id, updated_note)

@app.delete("/notes/{note_id}")
async def delete_note(note_id: int):
    existing = await crud.get_note(database, note_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Note not found")
    return await crud.delete_note(database, note_id)
