from .models import notes
from .schemas import NoteCreate, NoteUpdate
from sqlalchemy import select
from databases import Database

async def get_notes(db: Database):
    query = select(notes)
    return await db.fetch_all(query)

async def get_note(db: Database, note_id: int):
    query = select(notes).where(notes.c.id == note_id)
    return await db.fetch_one(query)

async def create_note(db: Database, note: NoteCreate):
    query = notes.insert().values(title=note.title, content=note.content)
    note_id = await db.execute(query)
    return {**note.dict(), "id": note_id}

async def update_note(db: Database, note_id: int, note: NoteUpdate):
    query = notes.update().where(notes.c.id == note_id).values(title=note.title, content=note.content)
    await db.execute(query)
    return {**note.dict(), "id": note_id}

async def delete_note(db: Database, note_id: int):
    query = notes.delete().where(notes.c.id == note_id)
    await db.execute(query)
    return {"msg": f"Note {note_id} deleted"}
