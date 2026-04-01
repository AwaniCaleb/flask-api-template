from flask import Flask
from .config import config_by_name
from .extensions import db, migrate, cors, jwt


def create_app(config_name="dev"):
    """Application factory for the REST API."""
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Enable CORS
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})

    # Import and register the V1 API blueprint
    from app.api.v1 import api_v1_bp

    app.register_blueprint(api_v1_bp, url_prefix="/api/v1")

    return app
