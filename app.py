from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Ruta raíz
@app.route('/')
def home():
    return "Microservicio activo y conectado a la base de datos!"

# Ruta para obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    conexion = sqlite3.connect('datos.db')
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM usuarios")
    filas = cursor.fetchall()
    
    usuarios = [{"id": fila[0], "nombre": fila[1], "edad": fila[2]} for fila in filas]
    conexion.close()
    
    return jsonify(usuarios)

# Ruta para agregar un nuevo usuario
@app.route('/usuarios', methods=['POST'])
def agregar_usuario():
    datos = request.json
    nombre = datos.get('nombre')
    edad = datos.get('edad')
    
    if not nombre or not edad:
        return jsonify({"error": "Faltan datos"}), 400
    
    conexion = sqlite3.connect('datos.db')
    cursor = conexion.cursor()
    
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, edad))
    conexion.commit()
    conexion.close()
    
    return jsonify({"mensaje": "Usuario agregado exitosamente"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
