from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import json
import os


login_bp = Blueprint("login", __name__)


@login_bp.route('/login_driver', methods=['GET', 'POST'])
def login_driver():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
		# Placeholder authentication: accept non-empty credentials
		# with open("driver.json", "r") as f:
		# 	dati = json.load(f)
		
		# hash_saved = dati["password"]

		# if ((not email) and (check_password_hash(hash_saved, password))):
		if not (email and password):
			flash('Inserisci email e password.')
			return render_template('login_driver.html')

		# Carica driver dal file JSON e cerca corrispondenza
		json_path = os.path.join(os.path.dirname(__file__), '..', 'cartella_json', 'driver.json')
		json_path = os.path.normpath(json_path)
		users = []
		try:
			with open(json_path, 'r', encoding='utf-8') as f:
				try:
					users = json.load(f)
				except json.JSONDecodeError:
					f.seek(0)
					raw = f.read().strip()
					if raw.startswith('{') and '}{' in raw:
						fixed = '[' + raw.replace('}{', '},{') + ']'
						try:
							users = json.loads(fixed)
						except Exception:
							users = []
					else:
						users = []
		except FileNotFoundError:
			users = []

		if not isinstance(users, list):
			if isinstance(users, dict):
				users = [users]
			else:
				users = []

		matched = None
		for u in users:
			if u.get('email') == email and u.get('password') == password:
				matched = u
				break

		if matched:
			session['user'] = {"id": matched.get('id'), "role": "driver", "name": matched.get('name'), "email": matched.get('email')}
			flash('Login autista effettuato con successo!')
			return redirect(url_for('main.homepage'))
		else:
			flash('Account autista non trovato. Controlla email/password o registrati.')
			return render_template('login_driver.html')
	return render_template('login_driver.html')


@login_bp.route('/login_passenger', methods=['GET', 'POST'])
def login_passenger():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')
		if not (email and password):
			flash('Inserisci email e password.')
			return render_template('login_passenger.html')

		# Carica passeggeri dal file JSON e cerca corrispondenza
		json_path = os.path.join(os.path.dirname(__file__), '..', 'cartella_json', 'passenger.json')
		json_path = os.path.normpath(json_path)
		users = []
		try:
			with open(json_path, 'r', encoding='utf-8') as f:
				try:
					users = json.load(f)
				except json.JSONDecodeError:
					f.seek(0)
					raw = f.read().strip()
					if raw.startswith('{') and '}{' in raw:
						fixed = '[' + raw.replace('}{', '},{') + ']'
						try:
							users = json.loads(fixed)
						except Exception:
							users = []
					else:
						users = []
		except FileNotFoundError:
			users = []

		if not isinstance(users, list):
			if isinstance(users, dict):
				users = [users]
			else:
				users = []

		matched = None
		for u in users:
			if u.get('email') == email and u.get('password') == password:
				matched = u
				break

		if matched:
			session['user'] = {"id": matched.get('id'), "role": "passenger", "name": matched.get('name'), "email": matched.get('email')}
			flash('Login passeggero effettuato con successo!')
			return redirect(url_for('main.homepage'))
		else:
			flash('Account passeggero non trovato. Controlla email/password o registrati.')
			return render_template('login_passenger.html')
	return render_template('login_passenger.html')


@login_bp.route('/login', methods=['GET'])
def login_index():
	return render_template('login_index.html')


@login_bp.route('/logout')
def logout():
	session.pop('user', None)
	flash('Sei stato disconnesso.')
	return redirect(url_for('main.homepage'))