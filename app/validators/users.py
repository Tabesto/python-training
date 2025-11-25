from __future__ import annotations

from datetime import datetime
from typing import Any

from cerberus import Validator


def _coerce_iso_datetime(value: Any):
    if value in (None, "", False):
        return None
    if isinstance(value, datetime):
        return value
    if isinstance(value, (int, float)):
        raise ValueError("datetime must be an ISO-8601 string")
    if not isinstance(value, str):
        raise ValueError("datetime must be an ISO-8601 string")
    try:
        return datetime.fromisoformat(value)
    except ValueError as exc:
        raise ValueError("datetime must be an ISO-8601 string") from exc


USER_CREATE_SCHEMA = {
    "name": {"type": "string", "required": True, "empty": False},
    "created_at": {
        "type": "datetime",
        "required": False,
        "nullable": True,
        "coerce": _coerce_iso_datetime,
    },
}


def validate_user_create(payload: dict[str, Any]) -> tuple[bool, dict[str, Any] | dict]:
    validator = Validator(USER_CREATE_SCHEMA)
    if not validator.validate(payload):
        return False, validator.errors
    return True, validator.document

