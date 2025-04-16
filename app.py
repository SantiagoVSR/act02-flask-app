from flask import Flask
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Obtener fecha y hora actual
    actual = datetime.now()
    fecha_formateada = actual.strftime("%d, %B, %Y, %H:%M:%S")

    # Leer el archivo desde la URL
    url = "https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt"
    response = requests.get(url)
    contenido = response.text

    # Procesar líneas y filtrar
    lineas = contenido.strip().split('\n')
    personas_filtradas = []

    for linea in lineas:
        partes = linea.split(';')
        if partes and partes[0][0] in {'3', '4', '5', '7'}:
            personas_filtradas.append(partes)

    # Crear tabla HTML
    tabla_html = """
    <h2>Personas filtradas (ID comienza con 3, 4, 5, 7)</h2>
    <table border="1" cellpadding="5">
        <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Email</th>
        </tr>
    """

    for persona in personas_filtradas:
        tabla_html += f"<tr><td>{persona[0]}</td><td>{persona[1]}</td><td>{persona[2]}</td><td>{persona[3]}</td></tr>"

    tabla_html += "</table>"

    return f"""
    <html>
        <body>
            <h1>¡Hola, mundo!</h1>
            <p>Fecha actual: <b>{fecha_formateada}</b></p>
            {tabla_html}
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
