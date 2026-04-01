import pytest
from app import create_app
from app.extensions import db


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # Create the app
    app = create_app("dev")

    # Override config for testing
    app.config.update(
        {
            "TESTING": True,
            # Use an in-memory SQLite database so tests are fast and isolated!
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        }
    )

    # Set up the application context
    with app.app_context():
        # Build the fake database
        db.create_all()

        # Pause here and hand the app over to the tests
        yield app

        # Tear down the database after tests are done
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """A test client for the app to simulate HTTP requests."""
    return app.test_client()
