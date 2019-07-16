import os
from flask import Flask, escape, request
from scraping import scrape

app = Flask(__name__)

produtos = [528476, 1858285078]

@app.route('/')
def ofertas():
    html = "<pre>"
    for pid in produtos:
        produto = scrape(pid)
        html += produto['html'] + '\n'

        print(produto)

    return html

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)