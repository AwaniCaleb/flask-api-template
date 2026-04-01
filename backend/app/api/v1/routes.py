from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.api.v1 import api_v1_bp
from app.extensions import db
from app.models import User
from app.decorators import admin_required


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


@api_v1_bp.route("/admin/dashboard", methods=["GET"])
@jwt_required()
@admin_required
def admin_dashboard():
    """A highly protected route for admins only."""
    return (
        jsonify(
            {
                "status": "success",
                "message": "Welcome to the Admin Dashboard!",
                "secret_data": "Here is data only admins can see.",
            }
        ),
        200,
    )


@api_v1_bp.route("/users", methods=["GET"])
@jwt_required()
@admin_required
def get_all_users():
    """Get a paginated list of all users (Admin only)."""

    # 1. Get query parameters from the URL (e.g., ?page=2&per_page=5)
    # If they aren't provided, default to page 1 and 10 items per page.
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    # 2. Query the database using SQLAlchemy's built-in paginate method
    # error_out=False ensures it returns an empty list instead of a 404 if the page exceeds the total
    pagination = User.query.paginate(page=page, per_page=per_page, error_out=False)

    # 3. Get the actual user objects for this specific page
    users = pagination.items

    # 4. Return the data AND the metadata the frontend needs to build pagination buttons
    return (
        jsonify(
            {
                "status": "success",
                "data": [user.to_dict() for user in users],  # Serialize each user!
                "meta": {
                    "current_page": pagination.page,
                    "per_page": pagination.per_page,
                    "total_pages": pagination.pages,
                    "total_items": pagination.total,
                    "has_next": pagination.has_next,
                    "has_prev": pagination.has_prev,
                },
            }
        ),
        200,
    )
