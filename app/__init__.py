from __future__ import annotations

from flask import Flask, Response

from app.repositories.users import init_db
from app.routes.users import users_bp


def create_app() -> Flask:
    app = Flask(__name__)

    register_blueprints(app)
    register_error_handlers(app)
    init_db()

    return app


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(users_bp)


def register_error_handlers(app: Flask) -> None:
    @app.errorhandler(404)
    def not_found(_error):
        return Response(
            '{"error":"resource_not_found"}',
            status=404,
            mimetype="application/json",
        )


app = create_app()

