import requests

url = "https://restrepo-comercial.onrender.com"
files = {"file": open("Prueba2_20250815.txt", "rb")}
response = requests.post(url, files=files)
print(response.text)
