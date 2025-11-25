from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    name: str
    created_at: datetime

