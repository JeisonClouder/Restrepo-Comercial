from flask import Flask, request, jsonify
import paramiko
import os
from tempfile import NamedTemporaryFile

app = Flask(__name__)

@app.route("/procesar", methods=["POST"])
def procesar():
    try:
        # Cargar la llave privada desde variable de entorno
        key_data = os.getenv("SSH_KEY")
        if not key_data:
            return jsonify({"error": "No se encontró la variable SSH_KEY"}), 500

        with NamedTemporaryFile(delete=False, mode="w") as key_file:
            key_file.write(key_data)
            key_path = key_file.name

        hostname = "192.168.0.150"  # IP del servidor
        username = "salesforce"
        remote_dir = "/home/shared/pendientetransmitir"

        key = paramiko.RSAKey.from_private_key_file(key_path)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=hostname, username=username, pkey=key)

        sftp = client.open_sftp()
        sftp.chdir(remote_dir)
        archivos = sftp.listdir()

        # Ejemplo: solo imprimir los nombres
        print("Archivos encontrados:", archivos)

        # Aquí podrías procesarlos y mandarlos a Salesforce por API REST

        sftp.close()
        client.close()

        return jsonify({"status": "ok", "archivos": archivos})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
