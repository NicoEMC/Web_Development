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

    🔹 Agregar Autenticación de Usuarios con MongoDB
    ✅ Objetivo: Permitir que más usuarios se registren y accedan con credenciales.
    ✅ Tecnologías: Flask + Flask-Login + MongoDB

    📌 ¿Qué podemos hacer?

    🔹 Registro de nuevos usuarios con email y contraseña.
    🔹 Hashear contraseñas con bcrypt para mayor seguridad.
    🔹 Iniciar sesión y guardar sesiones activas.
    🔹 Proteger rutas para usuarios autenticados.
    Ejemplo de flujo: 1️⃣ Un usuario crea una cuenta.
    2️⃣ Inicia sesión y accede al generador de gráficos.
    3️⃣ Puede ver sus archivos anteriores y descargarlos.

    🔹 Guardar Gráficos en la Base de Datos
    ✅ Objetivo: Permitir a los usuarios guardar y ver gráficos generados anteriormente.
    ✅ Cómo hacerlo:

    Guardar los gráficos generados en MongoDB en lugar de solo generarlos en static/plot.png.
    Permitir que el usuario descargue gráficos anteriores cuando quiera.
    📌 Flujo de usuario: 1️⃣ Sube un archivo y genera un gráfico.
    2️⃣ Se almacena en MongoDB junto con la fecha y datos usados.
    3️⃣ Puede descargar gráficos anteriores desde un historial.

    🔹 Agregar un Blog o Página de Noticias
    ✅ Objetivo: Tener una sección donde puedas compartir tutoriales, noticias o información sobre los gráficos.
    ✅ Cómo hacerlo:

    Crear una sección de blog en Flask con MongoDB.
    Permitir que los usuarios comenten y reaccionen a los artículos.
    Agregar una interfaz atractiva para la visualización de artículos.
    📌 Ejemplo de uso:

    Publicar artículos sobre el uso de gráficos.
    Explicar tendencias de datos que los usuarios pueden analizar.
    Agregar categorías y etiquetas para organizar el contenido.


    🔹 Agregar Soporte para Más Tipos de Archivos
    ✅ Objetivo: Permitir que los usuarios suban más formatos, como JSON o Google Sheets.
    ✅ Opciones:

    Permitir subir archivos .json con datos estructurados.
    Conectar la app a Google Sheets API para leer datos de hojas de cálculo en la nube.
    Agregar una vista previa de los datos antes de generar el gráfico.

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