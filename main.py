import sqlite3

from flask import Flask, render_template, request

from db import crear_db

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        telefono = request.form["telefono"]
        guardar_visita(telefono)
        count = contar_visitas(telefono)
        return render_template("index.html", count=count)
    return render_template("index.html")


@app.route("/registros", methods=["GET"])
def mostrar_registros():
    conn = sqlite3.connect("cafeteria.db")
    cursor = conn.cursor()
    cursor.execute("SELECT telefono, COUNT(*) AS conteo FROM visitas GROUP BY telefono")
    registros = cursor.fetchall()
    conn.close()
    return render_template("registros.html", registros=registros)


# Guardar visita en la base de datos
def guardar_visita(telefono):
    conn = sqlite3.connect("cafeteria.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO visitas (telefono) VALUES (?)", (telefono,))
    conn.commit()
    conn.close()


def contar_visitas(telefono):
    conn = sqlite3.connect("cafeteria.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM visitas WHERE telefono=?", (telefono,))
    count = cursor.fetchone()[0]
    conn.close()
    return count


if __name__ == "__main__":
    crear_db()
    app.run()
