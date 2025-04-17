url = "https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/..."
response = requests.get(url)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
