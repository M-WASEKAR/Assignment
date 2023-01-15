
# The below API print the price of Bitcoin in USD and GBP
# https://api.coindesk.com/v1/bpi/currentprice.json
# • Collect data from this API for 1 day at 5 minutes interval. I.e you will have at least
# 288 unique data points. Consecutive data points should not have same value.
# • Find the highest and lowest price of bitcoin from the collected data

import requests
bitcon_api_url ="https://api.coindesk.com/v1/bpi/currentprice.json"
reponse = requests.get(bitcon_api_url)
response_json =reponse.json()
print(response_json)
print(min(response_json))
print(max(response_json))


