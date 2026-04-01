from flask import request, jsonify
from flask_jwt_extended import create_access_token
from app.api.v1 import api_v1_bp
from app.extensions import db
from app.models import User


@api_v1_bp.route("/auth/register", methods=["POST"])
def register():
    """Register a new user and return their data."""
    # Get the JSON data sent by the frontend
    data = request.get_json()

    # 1. Basic Validation
    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Missing email or password"}), 400

    # 2. Check if user already exists
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "User with that email already exists"}), 409

    # 3. Create the new user
    new_user = User(email=data["email"])
    new_user.set_password(data["password"])

    # 4. Save to database
    db.session.add(new_user)
    db.session.commit()

    # 5. Return success response (using our to_dict method!)
    return (
        jsonify({"message": "User created successfully", "user": new_user.to_dict()}),
        201,
    )


@api_v1_bp.route("/auth/login", methods=["POST"])
def login():
    """Authenticate a user and return a JWT."""
    data = request.get_json()

    # 1. Basic Validation
    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Missing email or password"}), 400

    # 2. Find the user in the database
    user = User.query.filter_by(email=data["email"]).first()

    # 3. Check if user exists AND password is correct
    if not user or not user.check_password(data["password"]):
        return jsonify({"error": "Invalid email or password"}), 401

    # 4. Generate the JWT! We use the user's ID as their "identity" in the token
    # We convert it to a string because JWT identities should generally be strings
    access_token = create_access_token(identity=str(user.id))

    # 5. Return the token and user data
    return (
        jsonify(
            {
                "message": "Login successful",
                "access_token": access_token,
                "user": user.to_dict(),
            }
        ),
        200,
    )
