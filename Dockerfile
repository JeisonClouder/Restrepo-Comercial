# Etapa 1: Usar una imagen oficial y ligera de Python como base
FROM python:3.10-slim

# Etapa 2: Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Etapa 3: Copiar el archivo de dependencias e instalarlas
# Se hace en un paso separado para aprovechar el caché de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 4: Copiar todo el código de tu aplicación al contenedor
COPY . .

# Etapa 5: Exponer el puerto que tu aplicación usará
# Render asignará un puerto dinámicamente, pero es buena práctica declararlo
EXPOSE 5000

# Etapa 6: El comando para iniciar la aplicación usando el servidor Gunicorn
# Le dice a Gunicorn que escuche en todas las interfaces en el puerto 5000
# y que ejecute el objeto 'app' que se encuentra en el archivo 'app.py'
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]