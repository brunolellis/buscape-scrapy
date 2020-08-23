import os
from flask import Flask, escape, request
from scraping_json import scrape

app = Flask(__name__)

products = {
    "3323872": "https://www.buscape.com.br/carrinho-bebe/carrinho-de-bebe-chicco-london",
    "5666437": "https://www.buscape.com.br/carrinho-bebe/carrinho-de-bebe-burigotto-it",
    "2238843": "https://www.buscape.com.br/carrinho-bebe/carrinho-de-bebe-burigotto-up"
}

@app.route('/')
def ofertas():
    html = "<body><table cellspacing=1 cellpadding=6 border=1>"
    html += "<tr><th>produto</th><th>preço atual</th><th>menor preço</th></tr>"
    for pid in products:
        prices = scrape(pid)
        url = products[pid]
        name = url.split("/")[-1]
        html += f"<tr><td><a href='{url}' target='_blank'>{name}</a></td><td align='right'>{prices[0]}</td><td align='right'>{prices[1]}</td></tr>"

    html += "</table></body>"
    return html

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
