from flask import Blueprint, render_template, request, redirect, url_for, flash, session   # Importa gli strumenti necessari da Flask
import json
import random as Random
import os
from werkzeug.utils import secure_filename

# allowed extensions for images
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Crea un Blueprint per organizzare le route relative alla registrazione/autista
registration_bp = Blueprint("registration", __name__)
# id_driver =0
# id_passenger=0
# id_school=0

@registration_bp.route("/index.html")
def registration_index():
    return render_template("index.html")

# Route per la registrazione dell'autista
@registration_bp.route("/registration_driver", methods=['GET', 'POST'])
def registration_driver():
    if request.method == 'POST':
        # Recupera i dati dal form inviato
        name = request.form['name']
        surname = request.form['surname']
        age_str = request.form['age']
        password = request.form['password']
        email = request.form['email'] # Ci manca da inserire l'Id e la data di creazione account
        license = request.form['license']

        # Valida l'età
        try:
            age = int(age_str)
            if age < 18 or age > 70:
                flash('L\'età deve essere compresa tra 18 e 70 anni.')
                return render_template('registration_driver.html')
        except ValueError:
            flash('L\'età deve essere un numero valido.')
            return render_template('registration_driver.html')

        # assegna un id unico
        driver_id = Random.randint(1, 1000000)

        # prepara struttura dati base
        driver_data = {
            "id": driver_id,
            "name": name,
            "surname": surname,
            "age": age,
            "password": password,
            "email": email,
            "license": license,
            "license_front": None,
            "license_back": None
        }

        # Gestione upload file patente
        upload_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'static', 'uploads', 'licenses'))
        os.makedirs(upload_dir, exist_ok=True)

        front_file = request.files.get('license_front')
        back_file = request.files.get('license_back')

        if front_file and front_file.filename:
            if allowed_file(front_file.filename):
                ext = secure_filename(front_file.filename).rsplit('.', 1)[1].lower()
                saved_name = f"{email}_{license}_front.{ext}"
                front_path = os.path.join(upload_dir, saved_name)
                try:
                    front_file.save(front_path)
                    # salvo il percorso relativo al folder static per poterlo servire
                    driver_data['license_front'] = os.path.join('static', 'uploads', 'licenses', saved_name).replace('\\','/')
                except Exception as e:
                    flash('Errore nel salvataggio della foto patente (fronte).')
                    return render_template('registration_driver.html')
            else:
                flash('Formato file non supportato per la foto patente (fronte).')
                return render_template('registration_driver.html')

        if back_file and back_file.filename:
            if allowed_file(back_file.filename):
                ext = secure_filename(back_file.filename).rsplit('.', 1)[1].lower()
                saved_name = f"{email}_{license}_back.{ext}"
                back_path = os.path.join(upload_dir, saved_name)
                try:
                    back_file.save(back_path)
                    driver_data['license_back'] = os.path.join('static', 'uploads', 'licenses', saved_name).replace('\\','/')
                except Exception as e:
                    flash('Errore nel salvataggio della foto patente (retro).')
                    return render_template('registration_driver.html')
            else:
                flash('Formato file non supportato per la foto patente (retro).')
                return render_template('registration_driver.html')

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

        # id_driver += 1
        flash('Registrazione avvenuta con successo!')
        # Imposta lo stato di sessione per considerare l'utente loggato dopo la registrazione
        session['user'] = {"id": driver_data['id'], "role": "driver", "name": name, "email": email}
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
        age_str = request.form['age']
        password = request.form['password']
        email = request.form['email']

        # Valida l'età
        try:
            age = int(age_str)
            if age < 18 or age > 70:
                flash('L\'età deve essere compresa tra 18 e 70 anni.')
                return render_template('registration_passenger.html')
        except ValueError:
            flash('L\'età deve essere un numero valido.')
            return render_template('registration_passenger.html')

        passenger_data = {
            "id": Random.randint(1, 1000000),
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

        # id_passenger += 1
        flash('Registrazione avvenuta con successo!')
        session['user'] = {"id": passenger_data['id'], "role": "passenger", "name": name, "email": email}
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
            "id": Random.randint(1, 1000000),
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

        # id_school += 1
        flash('Registrazione avvenuta con successo!')
        session['user'] = {"id": school_data['id'], "role": "school", "name": name}
        return redirect(url_for('registration.registration_school_success'))
    return render_template("registration_school.html")

@registration_bp.route("/registration_school_success")
def registration_school_success():
    return render_template("registration_school_success.html")