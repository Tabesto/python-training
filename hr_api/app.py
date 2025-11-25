# app.py
from flask import Flask, jsonify
from routes.company import bp_companies

def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    # Blueprints
    app.register_blueprint(bp_companies)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
