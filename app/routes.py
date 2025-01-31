from flask import Blueprint, render_template, request, redirect, url_for, session, send_file
from app.utils import process_file, get_columns, login_required
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """
    Página principal. Redirige al login si no hay sesión activa.
    """
    if 'user' not in session:  # Verifica si el usuario está autenticado
        return redirect(url_for('auth.login'))  # Redirige al login
    return render_template('index.html')  # Muestra la página principal

@main.route('/upload', methods=['POST'])
@login_required
def upload_file():
    """
    Procesa la subida de un archivo.
    """
    if 'file' not in request.files:
        return render_template('index.html', error="No se seleccionó ningún archivo.")

    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', error="El archivo subido está vacío.")

    filepath = os.path.join('uploads', file.filename)
    file.save(filepath)

    try:
        # Obtener las columnas válidas del archivo
        columns = get_columns(filepath)
        return render_template('select_columns.html', columns=columns, filepath=filepath)
    except Exception as e:
        return render_template('index.html', error=f"Error al procesar el archivo: {str(e)}")


@main.route('/generate', methods=['POST'])
@login_required
def generate_graph():
    """
    Genera un gráfico basado en las columnas y el tipo seleccionado por el usuario.
    """
    filepath = request.form.get('filepath')
    x_column = request.form.get('x_column')
    y_column = request.form.get('y_column')
    chart_type = request.form.get('chart_type')  # Tipo de gráfico seleccionado

    try:
        # Generar el gráfico
        plot_url = process_file(filepath, x_column, y_column, chart_type)
        return render_template('select_columns.html', 
                               plot_url=plot_url,
                               filepath=filepath, 
                               columns=get_columns(filepath),
                               download_url=url_for('main.download_file')
                               )
    except Exception as e:
        return render_template('select_columns.html', 
                               error=f"Error al generar el gráfico: {str(e)}", 
                               filepath=filepath, 
                               columns=get_columns(filepath))
        
@main.route('/download')
@login_required
def download_file():
    """
    Permite al usuario descargar la imagen generada del gráfico.
    Ahora permite elegir la ubicación de guardado en lugar de descargar automáticamente.
    """
    file_path = os.path.join(os.getcwd(), "app", "static", "plot.png")  # ✅ Ruta absoluta correcta
    
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True, download_name="grafico.png")  # ✅ Permite elegir el destino
    else:
        return "❌ No se encontró la imagen. Genera un gráfico primero.", 404
