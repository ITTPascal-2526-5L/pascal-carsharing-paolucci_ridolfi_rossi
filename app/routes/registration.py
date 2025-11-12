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
        json_path = 'app/cartella_json/driver.json'

        # Carica il contenuto esistente in modo robusto e appendi il nuovo oggetto
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    # Il file esiste ma non è un JSON valido: proviamo a sistemare casi come '}{' tra oggetti
                    f.seek(0)
                    raw = f.read().strip()
                    if raw.startswith('{') and '}{' in raw:
                        fixed = '[' + raw.replace('}{', '},{') + ']'
                        try:
                            data = json.loads(fixed)
                        except Exception:
                            data = []
                    else:
                        data = []
        except FileNotFoundError:
            data = []

        # Assicuriamoci che i dati siano una lista
        if not isinstance(data, list):
            if isinstance(data, dict):
                data = [data]
            else:
                data = []

        data.append(driver_data)

        # Scriviamo indietro l'array completo (sovrascrivendo il file)
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

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

        json_path = 'app/cartella_json/passenger.json'

        # Carica il contenuto esistente in modo robusto e appendi il nuovo oggetto
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    # Il file esiste ma non è un JSON valido: proviamo a sistemare casi come '}{' tra oggetti
                    f.seek(0)
                    raw = f.read().strip()
                    if raw.startswith('{') and '}{' in raw:
                        fixed = '[' + raw.replace('}{', '},{') + ']'
                        try:
                            data = json.loads(fixed)
                        except Exception:
                            data = []
                    else:
                        data = []
        except FileNotFoundError:
            data = []

        data.append(passenger_data)

        # Scriviamo indietro l'array completo (sovrascrivendo il file)
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

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

        json_path = 'app/cartella_json/school.json'

        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    # Il file esiste ma non è un JSON valido: proviamo a sistemare casi come '}{' tra oggetti
                    f.seek(0)
                    raw = f.read().strip()
                    if raw.startswith('{') and '}{' in raw:
                        fixed = '[' + raw.replace('}{', '},{') + ']'
                        try:
                            data = json.loads(fixed)
                        except Exception:
                            data = []
                    else:
                        data = []
        except FileNotFoundError:
            data = []

        data.append(school_data)

        # Scriviamo indietro l'array completo (sovrascrivendo il file)
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        flash('Registrazione avvenuta con successo!')
        return redirect(url_for('registration.registration_school_success'))
    return render_template("registration_school.html")

@registration_bp.route("/registration_school_success")
def registration_school_success():
    return render_template("registration_school_success.html")