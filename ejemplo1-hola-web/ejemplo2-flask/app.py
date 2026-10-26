from flask import Flask
import socket
app = Flask(__name__)
@app.route("/")
def inicio():
    return f"<h1>Aplicacion Python en Docker</h1><p>Flask se ejecuta dentro de un contenedor.</p><p>Hostname: {socket.gethostname()}</p>"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
