@app.route('/')
def home():
    url = "https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt"
    try:
        response = requests.get(url)
        response.raise_for_status()
        contenido = response.text
    except Exception as e:
        return f"<h1>Error al obtener datos:</h1><pre>{e}</pre>"

    return f"<h1>Contenido obtenido:</h1><pre>{contenido}</pre>"
