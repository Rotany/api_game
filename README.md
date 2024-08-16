# Cave Game API

Este proyecto es una API construida con Flask para gestionar usuarios, puntuaciones y puntos de un juego llamado "Cave Game". Utiliza MongoDB como base de datos.
Estos son los pasos a seguir:

1.- Instalación

Sigue los siguientes pasos para instalar y configurar el proyecto en tu entorno local:

* Clona el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/cave-game-api.git
    cd cave-game-api
    ```

*Crea y activa un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

*Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

2.- Configuración

* Variables de Entorno**: Crea un archivo `.env` o establece las siguientes variables de entorno:
    - `MONGO_URL`: URL del servidor de MongoDB.
    - `MONGO_PORT`: Puerto del servidor de MongoDB.

* Archivo de Configuración de Gunicorn: 
   - `gunicorn_config.py`: Archivo de configuración para desplegar la API usando Gunicorn.

3.- Uso

*Ejecución Local
Puedes iniciar la aplicación localmente usando Flask:
```bash
python main.py

La aplicación estará disponible en http://127.0.0.1:5000/.

4.- Despliegue con Guarnicon
gunicorn -c gunicorn_config.py main:app

5.- Extructura del proyecto
cave-game-api/
│
├── mongo/
│   ├── __init__.py
│   ├── entities.py      Define las entidades: User, FinalScore, Points
│   ├── models.py        Define los modelos de las entidades para MongoDB
│   ├── mongo_client.py  Interacción directa con MongoDB (insert, update, etc.)
│   └── utils.py         Funciones de utilidad para conversión de documentos
│
├── .gitignore           Lista de archivos y directorios ignorados por git
├── gunicorn_config.py   Configuración para ejecutar la API con Gunicorn
├── main.py              Punto de entrada de la aplicación Flask
├── requirements.txt     Dependencias del proyecto
└── README.md            Este archivo

