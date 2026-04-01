def test_register_success(client):
    """Test that a user can register successfully."""
    response = client.post(
        "/api/v1/auth/register",
        json={"email": "newuser@test.com", "password": "securepassword"},
    )

    # Assertions (Checking if the API gave us the exact answers we expected)
    assert response.status_code == 201
    assert response.json["message"] == "User created successfully"
    assert response.json["user"]["email"] == "newuser@test.com"


def test_register_duplicate_email(client):
    """Test that registering an existing email fails."""
    # 1. Register the first time
    client.post(
        "/api/v1/auth/register",
        json={"email": "duplicate@test.com", "password": "password"},
    )

    # 2. Try to register again
    response = client.post(
        "/api/v1/auth/register",
        json={"email": "duplicate@test.com", "password": "password"},
    )

    assert response.status_code == 409
    assert response.json["error"] == "User with that email already exists"


def test_login_success(client):
    """Test that a registered user can log in and receive a JWT."""
    # 1. Create the user
    client.post(
        "/api/v1/auth/register",
        json={"email": "login@test.com", "password": "password"},
    )

    # 2. Log them in
    response = client.post(
        "/api/v1/auth/login", json={"email": "login@test.com", "password": "password"}
    )

    assert response.status_code == 200
    assert response.json["message"] == "Login successful"
    assert "access_token" in response.json  # Verify the JWT is there!
