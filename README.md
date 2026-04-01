# Full-Stack React + Flask REST API Boilerplate

A production-ready, decoupled full-stack boilerplate. This repository provides a highly secure Python/Flask backend API and a lightning-fast React/Vite frontend. It is the perfect foundation for building scalable web applications.

## 🏗️ Architecture
This project uses a decoupled architecture, meaning the frontend and backend are completely separate applications that communicate via HTTP requests using JSON.

```text
flask-api-template/
├── backend/            # Flask REST API (Python)
│   ├── app/            # Application factory & API routes
│   ├── migrations/     # Database schema versions
│   └── tests/          # Pytest automated test suite
└── frontend/           # React Single Page Application (Node.js)
    └── src/            # React components & Vite config
```

## ✨ Features

**Backend (Flask)**
* **Application Factory Pattern:** Highly scalable architecture.
* **API Versioning:** Blueprint-based versioning (`/api/v1/...`).
* **Stateless Authentication:** JSON Web Tokens (JWT) using `Flask-JWT-Extended`.
* **Role-Based Access Control (RBAC):** Custom `@admin_required` decorators.
* **Database ORM & Migrations:** `Flask-SQLAlchemy` (SQLite/PostgreSQL) and `Flask-Migrate`.
* **Pagination & Global Error Handling:** Predictable, safe JSON responses.
* **Automated Testing:** Pre-configured `pytest` suite with in-memory database testing.

**Frontend (React)**
* **Vite Build Tool:** Lightning-fast hot module replacement (HMR).
* **React:** Modern functional components and hooks.
* **Environment Configuration:** Pre-configured to talk to the Flask backend via `VITE_API_URL`.

---

## 🚀 Getting Started (Local Development)

To run this application locally, you will need two terminal windows open—one for the backend, and one for the frontend.

### Prerequisites
* Python 3.8+
* Node.js 18+

### 1. Start the Flask Backend
Open your first terminal and navigate to the backend folder:
```bash
cd backend

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env

# Initialize the database
flask db upgrade

# Run the server (defaults to port 5000)
flask run
```

### 2. Start the React Frontend
Open a second terminal and navigate to the frontend folder:
```bash
cd frontend

# Install Node dependencies
npm install

# Set up environment variables
echo "VITE_API_URL=http://127.0.0.1:5000/api/v1" > .env

# Run the Vite development server (defaults to port 5173)
npm run dev
```

### 3. Test the Connection
Open your browser and navigate to `http://localhost:5173`. Click the **"Ping Flask API"** button to verify the frontend is successfully communicating with the backend!

---

## 🧪 Running Automated Tests
The backend comes with a pre-configured `pytest` suite. To run the tests, ensure your virtual environment is active inside the `backend/` folder and run:
```bash
pytest
```
