from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.api.v1 import api_v1_bp
from app.extensions import db
from app.models import User


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


@api_v1_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    """A protected route to view user profile data."""
    # 1. Get the user ID from the JWT token
    current_user_id = get_jwt_identity()

    # 2. Fetch the user from the database
    user = db.session.get(User, int(current_user_id))

    # 3. If the user was deleted but the token is still active, handle it gracefully
    if not user:
        return jsonify({"error": "User not found"}), 404

    # 4. Return the secure user data
    return (
        jsonify(
            {
                "status": "success",
                "message": "You accessed a protected route!",
                "user": user.to_dict(),
            }
        ),
        200,
    )
