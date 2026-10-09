from functools import wraps

from flask import (
    Blueprint, render_template, request, redirect,
    url_for, flash, abort
)
from flask_login import (
    login_user, logout_user, login_required, current_user
)
from sqlalchemy import select

from app.extensions import db
from app.models import User

auth = Blueprint("auth", __name__)


def role_required(*allowed_roles):
    def decorator(view_function):
        @wraps(view_function)
        @login_required
        def wrapped_view(*args, **kwargs):
            if current_user.role not in allowed_roles:
                abort(403)
            return view_function(*args, **kwargs)
        return wrapped_view
    return decorator


@auth.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("auth.dashboard"))

    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not full_name or not email or not password:
            flash("Please fill in all required fields.", "error")
            return render_template("register.html")

        if len(full_name) > 120 or len(email) > 150:
            flash("Name or email is too long.", "error")
            return render_template("register.html")

        if "@" not in email or "." not in email.rsplit("@", 1)[-1]:
            flash("Please enter a valid email address.", "error")
            return render_template("register.html")

        if len(password) < 10:
            flash("Password must be at least 10 characters.", "error")
            return render_template("register.html")

        existing_user = db.session.scalar(
            select(User).where(User.email == email)
        )

        if existing_user:
            flash("An account with that email already exists.", "error")
            return render_template("register.html")

        user = User(
            full_name=full_name,
            email=email,
            role="parent",
        )
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash("Your Parent/Guardian account was created successfully.", "success")
        return redirect(url_for("auth.dashboard"))

    return render_template("register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("auth.dashboard"))

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        user = db.session.scalar(
            select(User).where(User.email == email)
        )

        if user and user.is_active and user.check_password(password):
            login_user(user)
            return redirect(url_for("auth.dashboard"))

        flash("Invalid email or password.", "error")

    return render_template("login.html")


@auth.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("auth.login"))


@auth.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)