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

mnCost = config.mnCost
fileName = config.coinName
gravapi = 'https://graviex.net/api/v2/tickers/coinbtc.json'
gravprice = requests.get(gravapi, verify=False)
btcapi = 'https://api.coinmarketcap.com/v2/ticker/1/'
btcprice = requests.get(btcapi)
btcvalue = btcprice.json()['data']['quotes']['USD']['price']
coinvalue = gravprice.json()['ticker']['last']
coinbtcvol = gravprice.json()['ticker']['volbtc']
coinvol = gravprice.json()['ticker']['vol']
coinusdvol = float(coinbtcvol) * float(btcvalue)
coinusdvalue = float(btcvalue) * float(coinvalue)
mnPrice = float(coinusdvalue) * float(mnCost)

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
	

	
data = {'mnPrice' : mnPrice, 'mnCost' : mnCost, 'coin' : fileName, 'mnroi' : mnroi, 'mncount' : mncount, 'dEUSD' : dailyEarningsUSD, 'dEBTC' : dailyEarningsBTC, 'dECOIN' : dailyEarningsCOIN, 'wEUSD' : weeklyEarningsUSD, 'wEBTC' : weeklyEarningsBTC, 'wECOIN' : weeklyEarningsCOIN, 'mEUSD' : monthlyEarningsUSD, 'mEBTC' : monthlyEarningsBTC, 'mECOIN' : monthlyEarningsCOIN, 'yEUSD' : yearlyEarningsUSD, 'yEBTC' : yearlyEarningsBTC, 'yCOIN' : yearlyEarningsCOIN, 'btcvalue' : btcvalue, 'coinvalue' : coinvalue, 'coinbtcvol' : coinbtcvol, 'coinvol' : coinvol, 'coinusdvol' : coinusdvol, 'coinusdvalue' : coinusdvalue}
    
writeToJson(fileName, data)

		
		
		
