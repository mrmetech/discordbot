import json
import asyncio
import requests


def getInfoCRU():


    gravapi = 'https://graviex.net/api/v2/tickers/scrivbtc.json'
    gravprice = requests.get(gravapi, verify=False)
    scrivvol = gravprice.json()['ticker']['vol']

	
    data = {'test' : scrivvol}
    
	  with open("scriv.json", 'w') as fp:
		    json.dump(data, fp)

		
		
