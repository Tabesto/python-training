from __future__ import annotations

import json
from typing import Any

from flask import Blueprint, Response, request

from app.services import users as user_service
from app.validators import users as user_validators

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.get("/<int:user_id>")
def get_user(user_id: int):
    user = user_service.get_user(user_id)
    if user is None:
        return Response(
            '{"error":"resource_not_found"}',
            status=404,
            mimetype="application/json",
        )
    body = user.model_dump_json(indent=2)
    return Response(body, mimetype="application/json")


@users_bp.post("")
def create_user():
    payload: dict[str, Any] | None = request.get_json(silent=True)
    if payload is None:
        return invalid_payload({"message": "body must be valid JSON"})
    is_valid, data_or_errors = user_validators.validate_user_create(payload)
    if not is_valid:
        return invalid_payload(data_or_errors)
    user = user_service.create_user(
        name=data_or_errors["name"],
        created_at=data_or_errors.get("created_at"),
    )
    body = user.model_dump_json(indent=2)
    return Response(body, status=201, mimetype="application/json")


@users_bp.delete("/<int:user_id>")
def delete_user(user_id: int):
    deleted = user_service.delete_user(user_id)
    if not deleted:
        return Response(
            '{"error":"resource_not_found"}',
            status=404,
            mimetype="application/json",
        )
    return Response(status=204)


def invalid_payload(details: Any) -> Response:
    body = json.dumps({"error": "invalid_payload", "details": details})
    return Response(body, status=400, mimetype="application/json")

