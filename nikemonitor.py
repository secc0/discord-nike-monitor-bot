import requests
import json
import time


INSTOCK = []

WEBHOOK = ''

headers = {
    
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36',
}

url = 'https://apigateway.nike.com.br/nike-bff/search/nav/genero/masculino/idade/adulto/tipodeproduto/calcados?page=2&sorting=relevance&resultsPerPage=40&scoringProfile=scoreByRanking&multiFilters=false'
r = requests.get(url, headers=headers)


def scrape_site():
    html = requests.get(url=url)
    output = json.loads(html.text)
    return output['products']


def discord_webhook(name, price, url):
        data = {
            'embeds': [{
                'name': name,
                'fields': [
                    {'name': 'Price', 'value': str(price)},
                    {'name': 'url', 'value': url}
                ]
            }]
        }
        result = requests.post(WEBHOOK, data=json.dumps(data), headers={'Content-type':'aplication/json'})
        print(result.status_code)


def comparison(item, start):
    if(item['id'] in INSTOCK) and (item['inStock'] == False):
        INSTOCK.remove(item['id'])

    elif(item['id'] not in INSTOCK) and (item['inStock'] == True):
        INSTOCK.append(item['id'])
        if start== 0:
            discord_webhook(
                name=item['name'],
                price=item['price'],
                url=item['url']
            )
            print()



""" start = 0
while True:
    products = scrape_site()
    for product in products:
        comparison(product, start)
    

    start = 0
    time.sleep(5) """
    
