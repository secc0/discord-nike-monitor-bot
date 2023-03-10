import requests
import json
from discord_webhook import DiscordWebhook, DiscordEmbed

url = "https://apigateway.nike.com.br/nike-bff/search/nav/genero/masculino/idade/adulto/tipodeproduto/calcados"

querystring = {"page": "2", "sorting": "relevance", "resultsPerPage": "40",
               "scoringProfile": "scoreByRanking", "multiFilters": "false"}

payload = ""
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
}

response = requests.request(
    "GET", url, data=payload, headers=headers, params=querystring)

data = json.loads(response.text)
products = data['products']

for product in products:
    message = f"{product['name']} - R$ {product['price']}"
    webhook = DiscordWebhook(
        url='urldochat',
        content=message
    )
    response = webhook.execute()
