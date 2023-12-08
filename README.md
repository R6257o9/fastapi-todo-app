# FastAPI TODO App

## Instalacion

### Python3

Se necesita al menos _Python v3.10_ o superior para correr adecuadamente la app.

```bash
sudo apt install python3 python3-pip python3-venv
```

### Virtual Environment (Activar)

```bash
python3 -m venv .venv-app
source .venv-app/bin/activate
```

### Configurar archivo .env

Para configurar el archivo .env en el backend, cree un archivo .env y agregue lo siguiente en el archivo .env

```python
JWT_SECRET_KEY=<RAMDOM_STRING>
JWT_REFRESH_SECRET_KEY=<RANDOM_SECTURE_LONG_STRING>
MONGO_CONNECTION_STRING=<MONGO_DB_CONNECTION_STRING>
# MONGO_CONNECTION_STRING=mongodb://172.28.87.20:27017/ -> conexion host utilizando WSL Ubuntu en Windows
# MONGO_CONNECTION_STRING=mongodb://localhost:27017/ -> conexion local en Windows/Linux

MONGO_DB_NAME=<RAMDOM_STRING>
MONGO_USERNAME=<RAMDOM_STRING>
MONGO_PASSWORD=<RAMDOM_STRING>

```

### Instalar librerias

1. A través de requirements.txt

`pip3 install -r requirements.txt`

### Run app

`uvicorn main:app --reload`

## Docker

### Run mongo image

`docker pull mongo:4.4-focal`

`docker run -p 27017:27017 mongo:4.4-focal`

### Dockerfile

Crear y correr la imagen localmente

`docker build --tag farm-todo-app-back:paris .`

`docker run -d -p 8000:8000 farm-todo-app-back:paris`

### DockerHub

Descargar la imagen de DockerHub:

`docker pull hugoogonz/farm-todo-app-back:paris`

Correr imagen descargada desde Docker:

`docker run --name farm-todo-app -d -p 8000:8000 hugoogonz/farm-todo-app-back:paris`
