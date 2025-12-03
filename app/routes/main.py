from flask import Blueprint, render_template, redirect

main_bp = Blueprint("main", __name__)

@main_bp.route("/") # Qui mettiamo la route
def homepage():
    # TODO: session.get('user').get('name', session.get('user').get('email'))
    return render_template("home.html")
    #return render_template("index.html")

