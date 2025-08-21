from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from app.models import Usuario
from app import db
from werkzeug.security import check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET'])
def mostrar_login():
    if 'usuario_id' in session:
        return redirect(url_for('main.index'))
    return render_template('login.html')  # Ajusta la ruta si es distinta

@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.form['usuario']
    password = request.form['password']

    if not username or not password:
        return jsonify({'success': False, 'message': 'Todos los campos son obligatorios.'})

    usuario = Usuario.query.filter_by(usuario=username.upper()).first()

    if usuario and check_password_hash(usuario.password_hash, password):
        session['usuario_id'] = usuario.id
        #flash('Has iniciado sesión correctamente', 'success')
        #return redirect(url_for('main.index'))
        return jsonify({'success': True, 'redirect': '/index'})  # o cualquier otra ruta
    else:
        #flash('Usuario o password incorrecto', 'danger')
        return jsonify({'success': False, 'message': 'Usuario o password incorrectos'})
        #return redirect(url_for('auth.login'))


@auth_bp.route('/logout')
def logout():
    session.clear()
    #flash('Sesión cerrada', 'info')
    return redirect(url_for('auth.login'))