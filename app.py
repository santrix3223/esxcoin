from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta raíz para verificar que el servidor está funcionando
@app.route('/')
def home():
    return "Microservicio activo en Render!"

# Endpoint para el saludo
@app.route('/saludo', methods=['GET'])
def saludo():
    nombre = request.args.get('nombre', 'Mundo')
    return jsonify({"mensaje": f"Hola, {nombre} desde Python en Render!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

