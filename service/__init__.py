"""Customer Accounts service application setup."""

from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    csp = {
        "default-src": "'self'",
        "script-src": "'self'",
        "style-src": "'self' 'unsafe-inline'",
        "img-src": "'self' data:",
    }

    talisman = Talisman(
        app,
        content_security_policy=csp,
        force_https=False,
        strict_transport_security=True,
        session_cookie_secure=False,
    )
    CORS(app, resources={r"/accounts/*": {"origins": "*"}})

    @app.get("/health")
    def health():
        return {"status": "ok"}, 200

    return app


app = create_app()
