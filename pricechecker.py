import requests
import json

price = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=solana%2Ckin&vs_currencies=gbp%2Cgbp")

print("The price of Solana currently is " + str(price.json()['solana']['gbp']))
print("")
print("The price of Kin currently is " + str(price.json()['kin']['gbp']))
