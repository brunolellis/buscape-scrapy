import requests

def scrape(product_id):
    base_url = 'https://www.buscape.com.br/ajax/product_desk?__pAct_=_get_ph&_ph_t=d&prodid=' + str(product_id)

    r = requests.get(base_url)
    json = r.json()

    current_price = json["currentPrice"]

    lowest_price = 9999999999
    for point in json["points"]:
        if point["y"]["value"] < lowest_price:
            lowest_price = point["y"]["value"]

    # print(lowest_price)
    # print(current_price)
    return current_price, lowest_price

# if __name__ == "__main__":
    # scrape(5666437)