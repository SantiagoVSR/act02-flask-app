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
        return f"<h1>Error al leer el archivo</h1><p>{e}</p>"

    lineas = contenido.strip().split('\n')
    todas_las_personas = []
    personas_filtradas = []

    for linea in lineas:
        partes = linea.strip().split(';')
        if len(partes) == 4:
            todas_las_personas.append(partes)
            if partes[0].strip() and partes[0].strip()[0] in {'3', '4', '5', '7'}:
                personas_filtradas.append(partes)

    # Tabla completa (debug)
    tabla_todos = "<h3>Todos los datos encontrados:</h3><table border='1'><tr><th>ID</th><th>Nombre</th><th>Apellido</th><th>Email</th></tr>"
    for p in todas_las_personas:
        tabla_todos += f"<tr><td>{p[0]}</td><td>{p[1]}</td><td>{p[2]}</td><td>{p[3]}</td></tr>"
    tabla_todos += "</table>"

    # Tabla filtrada
    tabla_filtrada = "<h2>Filtrados (ID empieza con 3, 4, 5, 7)</h2><table border='1'><tr><th>ID</th><th>Nombre</th><th>Apellido</th><th>Email</th></tr>"
    for p in personas_filtradas:
        tabla_filtrada += f"<tr><td>{p[0]}</td><td>{p[1]}</td><td>{p[2]}</td><td>{p[3]}</td></tr>"
    tabla_filtrada += "</table>"

    return f"""
    <html>
        <body>
            <h1>¡Hola desde Flask en Render!</h1>
            <p>Fecha: <b>{fecha_formateada}</b></p>
            {tabla_filtrada}
            <br><br>
            {tabla_todos}
        </body>
    </html>
    """

