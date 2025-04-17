from flask import Flask
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Obtener fecha y hora actual
    actual = datetime.now()
    fecha_formateada = actual.strftime("%d, %B, %Y, %H:%M:%S")

    # URL del archivo
    url = "https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        contenido = response.text
    except Exception as e:
        return f"<h1>Error al leer el archivo</h1><p>{e}</p>"

    # Procesar líneas y filtrar por ID que empiece con 3, 4, 5 o 7
    lineas = contenido.strip().split('\n')
    personas_filtradas = []

    for linea in lineas:
        partes = linea.strip().split(';')
        if len(partes) == 4 and partes[0] and partes[0][0] in {'3', '4', '5', '7'}:
            personas_filtradas.append(partes)

    # Crear tabla HTML
    tabla_html = """
    <h2>Personas filtradas (ID empieza con 3, 4, 5, 7)</h2>
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
