from rpc import *
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import config
import json
import asyncio
import requests
import time


rpc = get_rpc()

mncount = rpc.masternode('count')

# let some daemon time to unlock wallet
time.sleep(1)
btcapi = 'https://api.coinmarketcap.com/v2/ticker/1/'
btcprice = requests.get(btcapi)
btcvalue = btcprice.json()['data']['quotes']['USD']['price']

fileName = config.coinName
stockapi = 'https://api.coingecko.com/api/v3/coins/curium.json'
stockprice = requests.get(stockapi)
coinvalue = stockprice.json()['tickers'][0]['converted_last']['btc']
sxcvalue = stockprice.json()['tickers'][1]['converted_last']['btc']
chanvalue = stockprice.json()['tickers'][2]['converted_last']['btc']
stockvol = stockprice.json()['tickers'][0]['volume']  
sxcvol = stockprice.json()['tickers'][1]['volume']
chanvol = stockprice.json()['tickers'][2]['volume']
cruusdvalue = stockprice.json()['market_data']['current_price']['usd']
volvalue = stockprice.json()['market_data']['total_volume']['usd']
bvolvalue = stockprice.json()['market_data']['total_volume']['btc']

dailyEarningsUSD = (((1 / float(mncount)) * float(config.blockReward)) * float(config.blocksPerADay) * float(config.blockRewardForMasternodes) * float(coinvalue) * float(btcvalue))
dailyEarningsBTC = (((1 / float(mncount)) * float(config.blockReward)) * float(config.blocksPerADay)  * float(config.blockRewardForMasternodes) * float(coinvalue))
dailyEarningsCOIN = ((1 / float(mncount)) *  float(config.blockReward) * float(config.blocksPerADay) * float(config.blockRewardForMasternodes))
mnroi = ((1 / float(mncount)) *  float(config.blockReward) * float(config.blocksPerADay) * float(config.blockRewardForMasternodes) * 365) / 1000
	
weeklyEarningsUSD = dailyEarningsUSD * 7 
weeklyEarningsBTC = dailyEarningsBTC  * 7
weeklyEarningsCOIN = dailyEarningsCOIN * 7
	
monthlyEarningsUSD = weeklyEarningsUSD * 4
monthlyEarningsBTC = weeklyEarningsBTC * 4
monthlyEarningsCOIN = weeklyEarningsCOIN * 4
	
yearlyEarningsUSD = dailyEarningsUSD * 365 
yearlyEarningsBTC = dailyEarningsBTC * 365
yearlyEarningsCOIN = dailyEarningsCOIN * 365
	

	
data = {'mnroi' : mnroi, 'mncount' : mncount, 'dEUSD' : dailyEarningsUSD, 'dEBTC' : dailyEarningsBTC, 'dECOIN' : dailyEarningsCOIN,
	'wEUSD' : weeklyEarningsUSD, 'wEBTC' : weeklyEarningsBTC, 
	'wECOIN' : weeklyEarningsCOIN, 'mEUSD' : monthlyEarningsUSD, 'mEBTC' : monthlyEarningsBTC, 
	'mECOIN' : monthlyEarningsCOIN, 'yEUSD' : yearlyEarningsUSD, 'yEBTC' : yearlyEarningsBTC, 'yCOIN' : yearlyEarningsCOIN, 
	'btcvalue' : btcvalue, 'bvolvalue' : bvolvalue, 'volvalue' : volvalue, 'usdvalue' : cruusdvalue}
    

writeToJson(path, fileName, data)

		
		
		
