from flask import Flask, escape, request
from scraping import scrape

app = Flask(__name__)

produtos = [528476]

@app.route('/')
def ofertas():
    html = "<pre>"
    for pid in produtos:
        produto = scrape(pid)
        html += produto['html'] + '\n'

        print(produto)

    return html

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)