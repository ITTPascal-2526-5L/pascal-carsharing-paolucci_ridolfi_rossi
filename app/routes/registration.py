from flask import Blueprint, render_template, request, redirect, url_for, flash   # Importa gli strumenti necessari da Flask
import json

# Crea un Blueprint per organizzare le route relative alla registrazione/autista
registration_bp = Blueprint("registration", __name__)

# Route per la registrazione dell'autista
@registration_bp.route("/registration_driver", methods=['GET', 'POST'])
def registration_driver():
    if request.method == 'POST':
        # Recupera i dati dal form inviato
        name = request.form['name']
        surname = request.form['surname']
        age = request.form['age']
        password = request.form['password']
        email = request.form['email'] # Ci manca da inserire l'Id e la data di creazione account
        license = request.form['license']

        driver_data = {
            "name": name,
            "surname": surname,
            "age": age,
            "password": password,
            "email": email,
            "license": license
        }

        # Salva i dati nel file JSON nella cartella corretta
        with open('app/cartella_json/driver.json', mode='a+', encoding='utf-8') as f:
            json.dump(driver_data, f, indent=4, ensure_ascii=False)

        flash('Registrazione avvenuta con successo!')
        return redirect(url_for('registration.registration_driver_success'))  # Reindirizza alla pagina di successo
    # Se GET, mostra il form di registrazione
    return render_template("registration_driver.html")

@registration_bp.route("/registration_driver_success")
def registration_driver_success():
    return render_template("registration_driver_success.html")

# Route per la registrazione del passeggero
@registration_bp.route("/registration_passenger", methods=['GET', 'POST'])
def registration_passenger():
    if request.method == 'POST':
        name=request.form['name']
        surname = request.form['surname']
        age = request.form['age']
        password = request.form['password']
        email = request.form['email']

        passenger_data = {
            "name": name,
            "surname": surname,
            "age": age,
            "password": password,
            "email": email
        }

        with open('app/cartella_json/passenger.json', mode='a+', encoding='utf-8') as f:
            json.dump(passenger_data, f, indent=4, ensure_ascii=False)

        flash('Registrazione avvenuta con successo!')
        return redirect(url_for('registration.registration_passenger_success'))

    return render_template("registration_passenger.html")

@registration_bp.route("/registration_passenger_success")
def registration_passenger_success():
    return render_template("registration_passenger_success.html")

@registration_bp.route("/registration_school", methods=['GET', 'POST'])
def registration_school():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        suffix = request.form['suffix']

        school_data = {
            "name":name,
            "address":address,
            "suffix":suffix
        }

        with open('app/cartella_json/school.json', mode='a+', encoding='utf-8') as f:
            json.dump(school_data, f, indent=4, ensure_ascii=False)

        flash('Registrazione avvenuta con successo!')
        return redirect(url_for('registration.registration_school_success'))
    return render_template("registration_school.html")

@registration_bp.route("/registration_school_success")
def registration_school_success():
    return render_template("registration_school_success.html")