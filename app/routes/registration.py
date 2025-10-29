from flask import Blueprint, render_template, redirect

registration_bp = Blueprint("registration", __name__)

@registration_bp.route("/registration_driver")
def registration_driver():
    return render_template("registration_d.html")

@registration_bp.route("/registration_passenger")
def registration_passenger():
    return render_template("registration_p.html")

#Tutti i blueprints devono essere registrati nella creazione dell'applicativo

