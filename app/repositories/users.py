from __future__ import annotations

from datetime import datetime, timezone
import sqlite3

from app.config import DB_PATH
from app.models import User


def init_db() -> None:
    DB_PATH.touch(exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        cur = conn.execute("SELECT COUNT(*) FROM users")
        (count,) = cur.fetchone()
        if count == 0:
            conn.execute(
                "INSERT INTO users (user_id, name, created_at) VALUES (?, ?, ?)",
                (1, "Serge", datetime.now(timezone.utc).isoformat()),
            )
            conn.commit()


def fetch_user(user_id: int) -> User | None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT user_id, name, created_at FROM users WHERE user_id = ?",
            (user_id,),
        ).fetchone()
    if row is None:
        return None
    return User(
        user_id=row["user_id"],
        name=row["name"],
        created_at=datetime.fromisoformat(row["created_at"]),
    )


def insert_user(name: str, created_at: datetime) -> User:
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute(
            "INSERT INTO users (name, created_at) VALUES (?, ?)",
            (name, created_at.isoformat()),
        )
        user_id = cursor.lastrowid
        conn.commit()
    user = fetch_user(user_id)
    assert user is not None
    return user


def delete_user(user_id: int) -> bool:
    """Delete a user by ID. Returns True if user was deleted, False if not found."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
        conn.commit()
        return cursor.rowcount > 0

