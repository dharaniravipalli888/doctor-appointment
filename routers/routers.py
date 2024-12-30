from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from database import users_collection  # Import from database.py

auth = Blueprint("auth", __name__)

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if users_collection.find_one({"username": username}):
            flash("Username already exists!", "error")
        else:
            hashed_password = generate_password_hash(password)
            users_collection.insert_one({"username": username, "password": hashed_password})
            flash("Signup successful! Please log in.", "success")
            return redirect("/login")

    return render_template("signup.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = users_collection.find_one({"username": username})
        if user and check_password_hash(user["password"], password):
            session["username"] = username
            flash("Login successful!", "success")
            return redirect(url_for("auth.home"))  # Redirect to home route in auth blueprint
        else:
            flash("Invalid username or password!", "error")

    return render_template("login.html")

@auth.route("/home")
def home():
    if "username" not in session:
        flash("Please log in to access the homepage.")
        return redirect(url_for("auth.login"))
    
    return render_template("home.html", username=session["username"])

@auth.route("/logout")
def logout():
    session.pop("username", None)
    flash("Logged out successfully!", "success")
    return redirect(url_for("auth.login"))
