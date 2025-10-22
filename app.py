from flask import Flask, request, send_file
import os

app = Flask(__name__)

# Carpeta donde se guardarán los archivos
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "API de facturas en Render funcionando ✅"

# Endpoint para subir archivo
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file part", 400

    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    return f"Archivo {file.filename} subido correctamente", 200

# Endpoint para obtener archivo actual
@app.route("/archivo/<nombre>", methods=["GET"])
def get_file(nombre):
    filepath = os.path.join(UPLOAD_FOLDER, nombre)
    if os.path.exists(filepath):
        return send_file(filepath)
    return "Archivo no encontrado", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
