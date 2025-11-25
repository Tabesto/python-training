from __future__ import annotations

from datetime import datetime, timezone

from app.models import User
from app.repositories import users as user_repo


def get_user(user_id: int) -> User | None:
    return user_repo.fetch_user(user_id)


def create_user(name: str, created_at: datetime | None = None) -> User:
    created_at = created_at or datetime.now(timezone.utc)
    return user_repo.insert_user(name=name, created_at=created_at)


def delete_user(user_id: int) -> bool:
    """Delete a user by ID. Returns True if user was deleted, False if not found."""
    return user_repo.delete_user(user_id)

