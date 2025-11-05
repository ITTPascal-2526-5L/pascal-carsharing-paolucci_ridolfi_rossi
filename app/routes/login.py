from flask import Blueprint, render_template, request, redirect, url_for, flash   # Importa gli strumenti necessari da Flask

# Crea un Blueprint per organizzare le route relative alla registrazione/autista
registration_bp = Blueprint("registration", __name__)

# Route per il login dell'autista
@registration_bp.route("/driver_login", methods=['GET', 'POST'])
def driver_login():
    if request.method == 'POST':
        # Recupera i dati dal form di login
        username = request.form['username']
        password = request.form['password']
        # Sostituisci questa parte con la verifica reale delle credenziali
        if username == 'driver' and password == 'password123':
            return redirect(url_for('registration.dashboard'))  # Reindirizza alla dashboard se login corretto
        else:
            flash('Credenziali non valide. Riprova.')  # Mostra errore se login fallito
    # Se GET, mostra il form di login
    return render_template("registration_d.html")