# 1. Usa una imagen base oficial de Python
FROM python:3.9-slim

# 2. Establece un directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# 3. Copia el archivo de dependencias (requirements.txt)
# y ejecuta la instalación de las bibliotecas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copia el resto de tu código de aplicación
COPY . .

# 5. Especifica el puerto que expondrá la aplicación.
# Por convención, usaremos el puerto 8080.
EXPOSE 8080

# 6. Comando para iniciar la aplicación usando Gunicorn
# 'app:app' significa: módulo 'app' (app.py) : objeto Flask 'app' (app = Flask(__name__))
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]