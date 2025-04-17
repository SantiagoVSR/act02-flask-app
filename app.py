from flask import Flask
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = 'https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt'
    response = requests.get(url)
    contenido = response.text

    
    lineas = contenido.strip().split('\n')
    encabezado = lineas[0].split('|')
    datos_filtrados = []

    for linea in lineas[1:]:
        partes = linea.split('|')
        if partes[0][0] in ['3', '4', '5', '7']:
            datos_filtrados.append(partes)

    
    tabla_html = '<table border="1" cellpadding="5" cellspacing="0">'
    tabla_html += '<tr>' + ''.join(f'<th>{col}</th>' for col in encabezado) + '</tr>'
    for fila in datos_filtrados:
        tabla_html += '<tr>' + ''.join(f'<td>{celda}</td>' for celda in fila) + '</tr>'
    tabla_html += '</table>'

    actual = datetime.now()
    fecha_formateada = actual.strftime("%d, %B, %Y, %M, %H, %S")

    return f'<h2>¡Hola, Loja!</h2><p><b>{fecha_formateada}</b></p>{tabla_html}'


if __name__ == '__main__':
    app.run( host='0.0.0.0', port=5000)
