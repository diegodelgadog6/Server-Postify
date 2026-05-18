from datetime import datetime
import uuid
from sqlmodel import Relationship, SQLModel, Field

class LikeCreate(SQLModel):
    user_id: uuid.UUID
    post_id: uuid.UUID

class LikeRead(SQLModel):
    user_id: uuid.UUID
    post_id: uuid.UUID
    created_at: datetime
    