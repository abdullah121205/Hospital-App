import os

from dotenv import load_dotenv
from flask import Flask
from app.auth import auth
from app.patients import patients
from app.extensions import db, migrate, login_manager
from app.models import User, Patient, Doctor, Appointment

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if not app.config["SECRET_KEY"] or not app.config["SQLALCHEMY_DATABASE_URI"]:
        raise RuntimeError("Missing SECRET_KEY or DATABASE_URL in .env")

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(patients, url_prefix="/patients")

    @login_manager.user_loader
    def load_user(user_id):
        try:
            return db.session.get(User, int(user_id))
        except (TypeError, ValueError):
         return None

    @app.route("/")
    def home():
        return {
            "application": "PediaCare",
            "message": "Pediatric Hospital Management System API",
            "status": "running",
            "database": "configured"
        }

    return app