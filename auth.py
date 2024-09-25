from flask import Blueprint, render_template, url_for, request, flash, redirect
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)
db = sqlite3.connect("db.sqlite")


@auth.get("/login")
def login():
    return render_template("login.html")


@auth.post("/login")
def login_post():
    cursor = db.cursor()

    email = request.form.get("email")
    password = request.form.get("password")

    cursor.execute(
        "SELECT email, password FROM users WHERE email=?",
        (email),
    )

    user = cursor.fetchall()

    if not user or not check_password_hash(user[0][1], password):
        flash("Please check your login details and try again.")
        return redirect(url_for("auth.login"))

    return redirect(url_for("main.profile"))


@auth.get("/signup")
def signup():
    return render_template("signup.html")


@auth.post("/signup")
def signup_post():
    email = request.form.get("email")
    name = request.form.get("name")
    password = request.form.get("password")

    cursor = db.cursor()

    cursor.execute("SELECT email FROM users WHERE email='?'", (email,))
    user_exists = cursor.fetchall()

    if len(user_exists) != 0:
        flash("User Already Exists!")
        return url_for("auth.signup")
    else:
        cursor.execute(
            "INSERT INTO users VALUES (?,?,?)",
            (
                email,
                name,
                generate_password_hash(password, method="sha256"),
            ),
        )
    return redirect(url_for("auth.login"))


@auth.get("/logout")
def logout():
    return "<h1>Hi</h1>"
