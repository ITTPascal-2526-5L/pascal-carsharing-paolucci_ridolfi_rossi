from flask import Blueprint, render_template, redirect, session

main_bp = Blueprint("main", __name__)

@main_bp.route("/") # Qui mettiamo la route
def homepage():
    user = session.get('user')
    user_name = None
    if user:
        user_name = user.get('name') or user.get('email')

    return render_template("home.html", user_name=user_name)
    #return render_template("index.html")

