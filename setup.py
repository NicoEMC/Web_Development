import os

def setup_project():
    """
    Crea la estructura básica de carpetas necesarias para el proyecto Flask.
    Esto incluye carpetas para archivos subidos y archivos estáticos.
    """
    # Crear carpetas necesarias
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('app/static', exist_ok=True)
    os.makedirs('app/templates', exist_ok=True)

    print("Estructura básica creada:")
    print("- uploads/")
    print("- app/static/")
    print("- app/templates/")

if __name__ == '__main__':
    setup_project()