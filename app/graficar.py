import pandas as pd
import matplotlib
import matplotlib.dates as mdates  # Asegúrate de importar esta librería
matplotlib.use('Agg')  # Usar backend sin GUI
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def grafico_barras(dataframe, x_column, y_column):
    
    if not pd.api.types.is_numeric_dtype(dataframe[x_column]):
        try:
            dataframe[x_column] = pd.to_datetime(dataframe[x_column], errors='coerce')  # Conversión directa a fecha
            print(f"Fechas convertidas en la columna {x_column}:")
            print(dataframe[x_column].head())
        except Exception as e:
            raise ValueError(f"Error al convertir la columna {x_column} a formato fecha: {e}")
   
    # Crear figura y ejes
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Crear Gráfico de barras
    bars = ax.bar(dataframe[x_column], dataframe[y_column], width=0.8)  # Usa las fechas como eje x

    if not pd.api.types.is_numeric_dtype(dataframe[x_column]):
        try:
        # Configurar el formateador de fechas para mostrar solo 'YYYY-MM-DD'
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        except Exception as e:
            raise ValueError(f"Error al convertir la columna {x_column} a formato fecha: {e}")
    
    # Ajustar la rotación de etiquetas para mejor legibilidad
    plt.xticks(rotation=45)

    # Etiquetas y título
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_title('Gráfico de barras')
    
    
    #  **Añadir etiquetas de datos encima de las barras**
    for bar, value in zip(bars, dataframe[y_column]):
        ax.text(bar.get_x() + bar.get_width() / 2,  # Posición X (centro de la barra)
                value,  # Posición Y
                str(value),  # Texto de la etiqueta
                ha='center', va='bottom', fontsize=10, color='black')
        
    print("✅ Gráfico de barras generado con éxito.")
    
    return ax    


        
def grafico_lineas(dataframe, x_column, y_column):
    """
    Genera un gráfico de líneas con etiquetas de datos.

    Args:
        dataframe (pd.DataFrame): Datos a graficar.
        x_column (str): Nombre de la columna para el eje X.
        y_column (str): Nombre de la columna para el eje Y.

    Returns:
        ax: Objeto Axes de Matplotlib con el gráfico.
    """
    print("🔹 Generando gráfico de líneas...")

    # Convertir la columna de fechas si no es numérica
    if not pd.api.types.is_numeric_dtype(dataframe[x_column]):
        try:
            dataframe[x_column] = pd.to_datetime(dataframe[x_column], errors='coerce')
            print(f"✅ Fechas convertidas correctamente:\n{dataframe[x_column].head()}")
        except Exception as e:
            raise ValueError(f"❌ Error al convertir la columna {x_column} a formato fecha: {e}")

    # Crear figura y ejes
    fig, ax = plt.subplots(figsize=(12, 8))

    # Crear un gráfico de líneas con marcadores en cada punto
    ax.plot(dataframe[x_column], dataframe[y_column], marker='o', linestyle='-', color='b')


    if not pd.api.types.is_numeric_dtype(dataframe[x_column]):
        try:
        # Configurar el formateador de fechas para mostrar solo 'YYYY-MM-DD'
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        except Exception as e:
            raise ValueError(f"Error al convertir la columna {x_column} a formato fecha: {e}")

    # Ajustar la rotación de etiquetas para mejor legibilidad
    plt.xticks(rotation=45)

    # Etiquetas y título
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_title('Gráfico de líneas')

    # ✅ **Añadir etiquetas de datos en cada punto**
    for x, y in zip(dataframe[x_column], dataframe[y_column]):
        ax.text(x,
                y + (y * 0.02),  # Elevar la etiqueta un 2% del valor original
                str(y), ha='center', va='bottom', fontsize=10, color='black',
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3')  # Fondo blanco con borde negro)
        )
        
    print("✅ Gráfico de líneas generado con éxito.")
    return ax  # Retornar el objeto ax        



def grafico_dispersion(dataframe, x_column, y_column):
    """
    Genera un gráfico de dispersión con etiquetas de datos.

    Args:
        dataframe (pd.DataFrame): Datos a graficar.
        x_column (str): Nombre de la columna para el eje X.
        y_column (str): Nombre de la columna para el eje Y.

    Returns:
        ax: Objeto Axes de Matplotlib con el gráfico.
    """
    print("🔹 Generando gráfico de dispersión...")

    # Convertir la columna de fechas si no es numérica
    if not pd.api.types.is_numeric_dtype(dataframe[x_column]):
        try:
            dataframe[x_column] = pd.to_datetime(dataframe[x_column], errors='coerce')
            print(f"✅ Fechas convertidas correctamente:\n{dataframe[x_column].head()}")
        except Exception as e:
            raise ValueError(f"❌ Error al convertir la columna {x_column} a formato fecha: {e}")

    # Crear figura y ejes
    fig, ax = plt.subplots(figsize=(12, 8))

    # Crear el scatter plot
    ax.scatter(dataframe[x_column], dataframe[y_column], color='blue', alpha=0.7)

    # Configurar el formateador de fechas si es necesario
    if pd.api.types.is_datetime64_any_dtype(dataframe[x_column]):
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
        plt.xticks(rotation=45)

    # Etiquetas y título
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_title('Gráfico de dispersión')

    # ✅ **Añadir etiquetas de datos**
    for x, y in zip(dataframe[x_column], dataframe[y_column]):
        ax.text(
            x, y + (y * 0.02),  # Elevar la etiqueta un poco
            str(y), 
            ha='center', va='bottom', fontsize=10, color='black',
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3')  # Fondo blanco con borde negro
        )

    print("✅ Gráfico de dispersión generado con éxito.")
    return ax  # Retornar el objeto ax        



