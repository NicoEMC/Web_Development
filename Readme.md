# Generador de Gráficos

Este proyecto es una aplicación web desarrollada con Flask que permite a los usuarios subir un archivo CSV o Excel, procesar los datos y generar gráficos de manera automática. La aplicación está diseñada para ser escalable y puede ampliarse con nuevas funcionalidades en el futuro.

## Características
- Subida de archivos en formato CSV o Excel.
- Generación de gráficos automáticos basados en los datos del archivo.
- Interfaz de usuario sencilla y responsive.

## Requisitos
- Python 3.7 o superior.
- Entorno virtual para manejar las dependencias (recomendado).

## Instalación
1. Clona este repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    ```

2. Navega al directorio del proyecto:
    ```bash
    cd Web Development
    ```

3. Crea un entorno virtual:
    ```bash
    python -m venv venv
    ```

4. Activa el entorno virtual:
    - En Windows:
      ```bash
      venv\\Scripts\\activate
      ```
    - En Mac/Linux:
      ```bash
      source venv/bin/activate
      ```

5. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso
1. Inicia la aplicación:
    ```bash
    python run.py
    ```

2. Abre tu navegador y visita:
    [http://127.0.0.1:5000](http://127.0.0.1:5000)

3. Sube un archivo CSV o Excel y genera un gráfico automáticamente.

## Estructura del Proyecto
    project/
    │
    ├── app/                     # Carpeta principal de la aplicación
    │   ├── __init__.py          # Configuración de la aplicación Flask
    │   ├── auth.py              # Autentificación y más
    │   ├── routes.py            # Rutas principales de la aplicación
    │   ├── utils.py             # Funciones auxiliares (procesar archivo, generar gráficos)
    │   ├── graficar.py          # Gráficos 
    │   ├── static/              # Archivos estáticos como CSS, imágenes
    │   └── templates/           # Plantillas HTML
    │
    ├── uploads/                 # Carpeta para almacenar archivos subidos
    ├── run.py                   # Archivo principal para ejecutar la aplicación
    ├── database.py              # Conexión a MongoDB
    │── test_mongo.py            # Prueba de conexión con MongoDB
    │── Dockerfile               # Archivo para construir la imagen Docker
    │── docker-compose.yml       # Configuración de Docker Compose
    ├── requirements.txt         # Lista de dependencias del proyecto
    ├── .env                     # Variables de entorno (MONGO_URI)
    └── README.md                # Documentación del proyecto


## Próximas Actualizaciones
Este proyecto está diseñado para ser escalable. Las futuras actualizaciones pueden incluir:
- Validación avanzada de archivos subidos.
- Soporte para múltiples tipos de gráficos.
- Implementación de un sistema de autenticación (login).
- Integración con bases de datos para almacenar archivos y resultados.
- Despliegue en un servidor web para producción.

---

## Contribución (NO DISPONIBLE AÚN)
Si deseas contribuir a este proyecto:
1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad o corrección:
    ```bash
    git checkout -b nombre-de-la-rama
    ```
3. Realiza tus cambios y súbelos:
    ```bash
    git push origin nombre-de-la-rama
    ```
4. Abre un Pull Request explicando tus cambios.

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.