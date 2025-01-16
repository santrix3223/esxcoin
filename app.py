from flask import Flask, jsonify, render_template
import requests
from requests.auth import HTTPDigestAuth
import threading
import time

app = Flask(__name__)

# Configuración del dispositivo Hikvision
devices = [
    {"ip": "casahome2023.sytes.net", "username": "admin", "password": "Candelita@1981"}
]

# Lista para almacenar los eventos capturados
events = []

# Función para capturar eventos en tiempo real
def capture_events(device):
    url = f"http://{device['ip']}/ISAPI/Event/notification/alertStream"
    try:
        with requests.get(url, auth=HTTPDigestAuth(device['username'], device['password']), stream=True) as response:
            if response.status_code == 200:
                for line in response.iter_lines():
                    if line:
                        event_data = line.decode('utf-8')
                        events.append({"device": device['ip'], "event": event_data, "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')})
            else:
                print(f"Error al conectar con {device['ip']}: {response.status_code}")
    except Exception as e:
        print(f"Error con el dispositivo {device['ip']}: {e}")

# Iniciar captura de eventos en un hilo separado
def start_capture():
    for device in devices:
        threading.Thread(target=capture_events, args=(device,), daemon=True).start()

# Ruta para la interfaz del dashboard
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# Ruta para obtener eventos en tiempo real
@app.route('/events')
def get_events():
    return jsonify(events)

if __name__ == '__main__':
    start_capture()  # Inicia la captura de eventos al arrancar el servidor
    app.run(debug=True)
