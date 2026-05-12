import datetime
from sqlmodel import SQLModel, Field

class UserCreate(SQLModel):
    username: str
    name: str
    lastname: str
    email: str
    password: str

class UserRead(SQLModel):
    id: uuid.UUID
    username: str
    name: str
    lastname: str
    email: str
    password: str
    created_at: datetime
