from flask import Flask
import os
import time
import psycopg2

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "ventas")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

def conectar():
    for intento in range(10):
        try:
            return psycopg2.connect(
                host=DB_HOST,
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
        except psycopg2.OperationalError:
            time.sleep(2)
    raise RuntimeError("No fue posible conectar con PostgreSQL")

@app.route("/")
def inicio():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS productos (id SERIAL PRIMARY KEY, nombre TEXT, precio REAL)")
    cursor.execute("SELECT COUNT(*) FROM productos")
    cantidad = cursor.fetchone()[0]
    
    if cantidad == 0:
        cursor.execute("INSERT INTO productos (nombre, precio) VALUES ('Teclado', 450), ('Mouse', 280), ('Monitor', 3200)")
        conexion.commit()
        
    cursor.execute("SELECT nombre, precio FROM productos ORDER BY id")
    filas = cursor.fetchall()
    cursor.close()
    conexion.close()
    
    html = "<h1>Productos almacenados en PostgreSQL</h1><ul>"
    for nombre, precio in filas:
        html += f"<li>{nombre}: ${precio:.2f}</li>"
        
    html += "</ul>"
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
