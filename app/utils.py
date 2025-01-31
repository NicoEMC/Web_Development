import pandas as pd
import matplotlib
import matplotlib.dates as mdates  # Asegúrate de importar esta librería
matplotlib.use('Agg')  # Usar backend sin GUI
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
from functools import wraps
from flask import session, redirect, url_for, flash
import bcrypt
from app.graficar import grafico_barras, grafico_lineas, grafico_dispersion


def login_required(f):
    """
    Decorador para proteger rutas que requieren autenticación.

    Args:
        f (function): Función original.

    Returns:
        function: Función decorada.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash('Debes iniciar sesión para acceder a esta página.', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

def hash_password(password):
    """
    Genera un hash seguro para la contraseña.
    Args:
        password (str): Contraseña en texto plano.

    Returns:
        str: Hash de la contraseña.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password, hashed_password):
    """
    Verifica si una contraseña coincide con un hash.

    Args:
        password (str): Contraseña en texto plano.
        hashed_password (str): Hash almacenado.

    Returns:
        bool: True si coinciden, False de lo contrario.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)


def get_columns(filepath):
    """
    Extrae las columnas disponibles en el archivo subido, filtrando solo columnas numéricas o de tipo fecha.
    Detecta automáticamente columnas con formato de fecha solo si no son numéricas.

    Args:
        filepath (str): Ruta del archivo subido.

    Returns:
        list: Lista de nombres de columnas que son numéricas o de tipo fecha.
    """
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
    elif filepath.endswith('.xlsx'):
        df = pd.read_excel(filepath)
    else:
        raise ValueError("Formato de archivo no soportado")

    # Filtrar columnas numéricas y convertir solo las no numéricas a formato de fecha
    valid_columns = []
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            valid_columns.append(col)
        else:
            try:
                # Intentar convertir la columna a formato de fecha
                converted_col = pd.to_datetime(df[col], errors='coerce')
                if converted_col.notna().sum() > 0:  # Aceptar solo si hay valores válidos
                    valid_columns.append(col)
            except Exception:
                pass  # Ignorar si la conversión falla

    return valid_columns


def process_file(filepath, x_column, y_column, chart_type):
    """
    Genera un gráfico basado en las columnas y el tipo seleccionados.

    Args:
        filepath (str): Ruta del archivo subido.
        x_column (str): Nombre de la columna para el eje X.
        y_column (str): Nombre de la columna para el eje Y.
        chart_type (str): Tipo de gráfico a generar.

    Returns:
        str: Ruta relativa del gráfico generado.
    """
    # Leer el archivo dependiendo de su formato
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
    elif filepath.endswith('.xlsx'):
        df = pd.read_excel(filepath)
    else:
        raise ValueError("Formato de archivo no soportado")

    # # Intentar convertir automáticamente columnas no numéricas al formato de fecha
    # for col in df.columns:
    #     if not pd.api.types.is_numeric_dtype(df[col]):
    #         try:
    #             df[col] = pd.to_datetime(df[col], errors='coerce')
    #         except Exception:
    #             pass  # Ignorar si la conversión falla
    
    
    # Mostrar los valores originales de la columna de fechas
    print(f"Valores originales de la columna {x_column}:")
    print(df[x_column].head())
    # Convertir explícitamente la columna de fechas si no es numérica
    if not pd.api.types.is_numeric_dtype(df[x_column]):
        try:
            df[x_column] = pd.to_datetime(df[x_column], errors='coerce')  # Conversión directa a fecha
            print(f"Fechas convertidas en la columna {x_column}:")
            print(df[x_column].head())
        except Exception as e:
            raise ValueError(f"Error al convertir la columna {x_column} a formato fecha: {e}")

    # Identificar valores no convertidos
    non_converted = df[df[x_column].isna()][x_column]
    if not non_converted.empty:
        print("Valores no convertidos a fecha:")
        print(non_converted)

    # Ruta donde se guardará el gráfico
    plot_path = 'app/static/plot.png'

    # Generar el gráfico
    create_plot(df, plot_path, x_column, y_column, chart_type)

    # Retornar la ruta relativa para Flask
    return 'static/plot.png'


def create_plot(dataframe, plot_path, x_column, y_column, chart_type):
    """
    Genera un gráfico basado en dos columnas y un tipo de gráfico.

    Args:
        dataframe (pd.DataFrame): Datos a graficar.
        plot_path (str): Ruta para guardar el gráfico.
        x_column (str): Nombre de la columna para el eje X.
        y_column (str): Nombre de la columna para el eje Y.
        chart_type (str): Tipo de gráfico a generar.

    Returns:
        None
    """
    
    print(dataframe[[x_column, y_column]].head())
    plt.figure(figsize=(12, 8))  # Tamaño aumentado para mejor visualización

    # Generar el gráfico según el tipo seleccionado
    ax = None
    if chart_type == 'line':
        ax = grafico_lineas(dataframe, x_column, y_column)
        
    elif chart_type == 'bar':
        ax = grafico_barras(dataframe, x_column, y_column)

    elif chart_type == 'scatter':
        ax = grafico_dispersion(dataframe, x_column, y_column)
         
        
    else:
        raise ValueError("Tipo de gráfico no soportado")

    if ax is not None:
        # Formatear las fechas en el eje X
        if pd.api.types.is_datetime64_any_dtype(dataframe[x_column]):
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))  # Formato: día-mes-año
            plt.gcf().autofmt_xdate()  # Rotar las fechas automáticamente para mejor legibilidad

        # Guardar el gráfico asegurando que plt.close() se ejecuta correctamente
        plt.savefig(plot_path, bbox_inches='tight')
        plt.close()
        print("✅ Gráfico guardado correctamente en:", plot_path)
    else:
        print("❌ Error: No se pudo generar el gráfico porque 'ax' es None.")

    print(dataframe[[x_column, y_column]].head())
