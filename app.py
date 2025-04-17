import os
from flask import Flask
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    actual = datetime.now()
    fecha_formateada = actual.strftime("%d, %B, %Y, %H:%M:%S")

    url = "https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt"

    try:
        response = requests.get(url)
        response.raise_for_status()
        contenido = response.text
    except Exception as e:
        return f"<h1>Error al obtener datos:</h1><pre>{e}</pre>"

    personas = []
    filtradas = []

    lineas = contenido.strip().split('\n')
    for linea in lineas:
        partes = linea.strip().split(';')
        if len(partes) == 4:
            id_val = partes[0].strip()
            personas.append(partes)
            if id_val and id_val[0] in ['3', '4', '5', '7']:
                filtradas.append(partes)

    def generar_tabla(datos, titulo):
        html = f"<h2>{titulo}</h2><table border='1' cellpadding='5'><tr><th>ID</th><th>Nombre</th><th>Apellido</th><th>Email</th></tr>"
        for p in datos:
            html += f"<tr><td>{p[0]}</td><td>{p[1]}</td><td>{p[2]}</td><td>{p[3]}</td></tr>"
        html += "</table>"
        return html

    return f"""
    <html>
        <head><title>Datos desde Gist</title></head>
        <body>
            <h1>¡Hola desde Flask en Render!</h1>
            <p>Fecha actual: <b>{fecha_formateada}</b></p>
            {generar_tabla(filtradas, "Filtrados (ID inicia con 3, 4, 5, 7)")}
            <hr>
            {generar_tabla(personas, "Todos los registros del archivo")}
        </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
