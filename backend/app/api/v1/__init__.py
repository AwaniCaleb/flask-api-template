from flask import Blueprint

# Name the blueprint specifically for v1
api_v1_bp = Blueprint("api_v1", __name__)

# Import routes at the bottom to attach them to the blueprint
from app.api.v1 import routes
