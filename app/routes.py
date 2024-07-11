from flask import Blueprint, jsonify, request, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from app.models import User
from app.utils import load_data, save_data
from app import db

bp = Blueprint('main', __name__)

@bp.route('/api/events', methods=['GET'])
def get_events():
    events = load_data()
    return jsonify(events)

@bp.route('/api/events', methods=['POST'])
def create_event():
    new_event = request.json
    events = load_data()
    new_event['id'] = str(max(int(event['id']) for event in events) + 1)
    events.append(new_event)
    save_data(events)
    return jsonify(new_event), 201

@bp.route('/api/events/types', methods=['GET'])
def get_event_types():
    events = load_data()
    types = list(set(event['type'] for event in events))
    return jsonify(types)

@bp.route('/api/events/repos', methods=['GET'])
def get_repos():
    events = load_data()
    repos = list(set(event['repo']['name'] for event in events))
    return jsonify(repos)

@bp.route('/api/events/users', methods=['GET'])
def get_users():
    events = load_data()
    users = list(set(event['actor']['login'] for event in events))
    return jsonify(users)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and password == user.password:  # In production, use proper password hashing
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')