# from pydantic import BaseModel

# class NoteBase(BaseModel):
#     title :str
#     content : str

# class NoteCreate(NoteBase):
#     title :str
#     content : str

from pydantic import BaseModel

class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteUpdate(NoteBase):
    pass

class Note(NoteBase):
    id: int
