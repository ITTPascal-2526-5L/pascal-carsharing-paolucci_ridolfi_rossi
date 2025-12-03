from flask import Blueprint, render_template
import os
import json

users_bp = Blueprint('users', __name__)


def _load_json(relpath):
    path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', relpath))
    try:
        with open(path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
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

    if isinstance(data, dict):
        return [data]
    if not isinstance(data, list):
        return []
    return data


@users_bp.route('/users')
def users_index():
    drivers = _load_json('cartella_json/driver.json')
    passengers = _load_json('cartella_json/passenger.json')
    schools = _load_json('cartella_json/school.json')
    return render_template('users.html', drivers=drivers, passengers=passengers, schools=schools)
