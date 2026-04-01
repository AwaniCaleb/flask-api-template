from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from app.extensions import db
from app.models import User


def admin_required(fn):
    """
    Custom decorator to verify admin status.
    Must be placed AFTER the @jwt_required() decorator.
    """

    @wraps(fn)
    def wrapper(*args, **kwargs):
        # 1. Get the user ID from the JWT token
        user_id = get_jwt_identity()

        # 2. Fetch the user from the database
        user = db.session.get(User, int(user_id))

        # 3. Check if the user exists and has the 'admin' role
        if not user or user.role != "admin":
            return (
                jsonify(
                    {
                        "error": "Forbidden",
                        "message": "Admin privileges are required to access this endpoint.",
                    }
                ),
                403,
            )

        # 4. If they are an admin, let them through!
        return fn(*args, **kwargs)

    return wrapper
