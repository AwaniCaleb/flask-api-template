from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone


class User(db.Model):
    """The User model for the API database."""

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)

    # Keeping role-based access control for the API
    role = db.Column(db.String(20), default="user")

    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def set_password(self, password):
        """Hashes the password before saving it to the database."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifies the password against the stored hash."""
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """
        Serializes the user object to a JSON-ready dictionary.
        CRITICAL: Never include the password_hash in this dictionary!
        """
        return {
            "id": self.id,
            "email": self.email,
            "role": self.role,
            # Convert the datetime object to an ISO 8601 string for the frontend
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }

    def __repr__(self):
        return f"<User {self.email}>"
