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

        # with open('../json_data/driver.json', 'w', encoding='utf-8') as f:
        #     json.dump(driver_data, f, indent=4)

        with open('pascal-carsharing-paolucci_ridolfi_rossi/app/json_data/driver.json', 'w', encoding='utf-8') as f:
            json.dump(driver_data, f, indent=4)

        # Qui si può aggiungere la logica per salvare i dati nel database
        flash('Registrazione avvenuta con successo!')  # Mostra un messaggio di conferma
        return redirect(url_for('registration.driver_login'))  # Reindirizza al login autista
    # Se GET, mostra il form di registrazione
    return render_template("registration_driver.html")

# Route per la dashboard dell'autista (pagina di benvenuto dopo il login)
# @registration_bp.route("/dashboard")
# def dashboard():
#     pass


# Route per la registrazione dell'autista
@registration_bp.route("/registration_passenger", methods=['GET', 'POST'])
def registration_passenger():
    pass