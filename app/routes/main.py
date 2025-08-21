from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Usuario
from app import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@main_bp.route('/index')
def index():
    if 'usuario_id' not in session:
        return redirect(url_for('auth.login'))

    usuario = Usuario.query.get(session['usuario_id'])
    return render_template('index.html', usuario=usuario)

@main_bp.route('/cambiar_password', methods=['POST'])
def cambiar_password():
    if 'usuario_id' not in session:
        return jsonify({'estado': 'danger', 'mensaje': 'Sesión no válida. Por favor inicia sesión nuevamente.'})

    usuario = Usuario.query.get(session['usuario_id'])

    password_actual = request.form.get('password_actual')
    nuevo_password = request.form.get('nuevo_password')
    confirmar_password = request.form.get('confirmar_password')

    if not check_password_hash(usuario.password_hash, password_actual):
        return jsonify({'estado': 'danger', 'mensaje': 'El password actual no es correcto.'})

    if nuevo_password != confirmar_password:
        return jsonify({'estado': 'warning', 'mensaje': 'Los nuevos passwords no coinciden.'})

    usuario.password_hash = generate_password_hash(nuevo_password)
    db.session.commit()

    return jsonify({'estado': 'success', 'mensaje': 'Password cambiado exitosamente.'})