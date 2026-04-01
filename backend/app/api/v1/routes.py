from flask import jsonify
from app.api.v1 import api_v1_bp


@api_v1_bp.route("/health", methods=["GET"])
def health_check():
    """V1 Health Check Endpoint."""
    return (
        jsonify(
            {
                "status": "success",
                "message": "API Version 1 is up and running smoothly!",
                "version": "1.0",
            }
        ),
        200,
    )
