from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def inicio():
    nombre_contenedor = socket.gethostname()
    return f'''
    <h1>Aplicación Python en Docker</h1>
    <p>Flask se ejecuta dentro de un contenedor.</p>
    <p>Hostname del contenedor: {nombre_contenedor}</p>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
