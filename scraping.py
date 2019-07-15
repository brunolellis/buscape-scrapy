from bs4 import BeautifulSoup
import requests

def scrape(product_id):
    base_url = 'http://www.buscape.com.br/prod_unico?idu=' + str(product_id)

    # Request URL and Beautiful Parser
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, "html.parser")

    offer = {}
    product = soup.find_all('h1', class_="product__title")[0]
    offer['title'] = product.contents[0]

    minor_price = soup.find_all('span', class_="minor-price")[0]
    price = minor_price.find("span", {"class":"value"}).contents[-1]
    offer['price'] = price

    offer['html'] = f"<a href='{base_url}'>{offer['title']} - R$ {offer['price']}"

    print(offer)

    return offer

if __name__ == "__main__":
    scrape()