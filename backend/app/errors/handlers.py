from flask import jsonify
from app.errors import errors_bp
from app.extensions import db


@errors_bp.app_errorhandler(400)
def bad_request_error(error):
    return (
        jsonify(
            {
                "error": "Bad Request",
                "message": "The server could not understand the request.",
            }
        ),
        400,
    )


@errors_bp.app_errorhandler(404)
def not_found_error(error):
    return (
        jsonify(
            {
                "error": "Not Found",
                "message": "The requested URL was not found on the server.",
            }
        ),
        404,
    )


@errors_bp.app_errorhandler(405)
def method_not_allowed_error(error):
    return (
        jsonify(
            {
                "error": "Method Not Allowed",
                "message": "The method is not allowed for the requested URL.",
            }
        ),
        405,
    )


@errors_bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()  # Rollback database session in case of a DB crash
    return (
        jsonify(
            {
                "error": "Internal Server Error",
                "message": "An unexpected error occurred on the server.",
            }
        ),
        500,
    )
