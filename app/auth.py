from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from database import get_database
from app.utils import check_password

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Maneja el inicio de sesión.
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Conectar a la base de datos
        db = get_database()
        user = db['users'].find_one({"username": username})

        # Verificar usuario y contraseña
        if user and check_password(password, user['password']):
            session['user'] = username
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Credenciales inválidas. Por favor, inténtalo de nuevo.', 'danger')

    return render_template('login.html')

@auth.route('/logout')
def logout():
    """
    Maneja el cierre de sesión.
    """
    session.pop('user', None)  # Eliminar usuario de la sesión
    flash('Has cerrado sesión exitosamente.', 'info')
    return redirect(url_for('auth.login'))