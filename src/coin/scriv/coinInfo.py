from rpc import *
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import config
import json
import asyncio
import requests
import time


async rpc = get_rpc()

mncount = rpc.masternode('count')

# let some daemon time to unlock wallet
time.sleep(1)

fileName = config.coinName
gravapi = 'https://graviex.net/api/v2/tickers/scrivbtc.json'
gravprice = requests.get(gravapi, verify=False)
btcapi = 'https://api.coinmarketcap.com/v2/ticker/1/'
btcprice = requests.get(btcapi)
btcvalue = btcprice.json()['data']['quotes']['USD']['price']
scrivvalue = gravprice.json()['ticker']['last']
scrivbtcvol = gravprice.json()['ticker']['volbtc']
scrivvol = gravprice.json()['ticker']['vol']
scrivusdvol = float(scrivbtcvol) * float(btcvalue)
scrivusdvalue = float(btcvalue) * float(scrivvalue)

dailyEarningsUSD = (((1 / float(mncount)) * float(config.blockReward)) * float(config.blocksPerADay) * float(config.blockRewardForMasternodes) * float(scrivvalue) * float(btcvalue))
dailyEarningsBTC = (((1 / float(mncount)) * float(config.blockReward)) * float(config.blocksPerADay)  * float(config.blockRewardForMasternodes) * float(scrivvalue))
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
	

	
data = {'mnroi' : mnroi, 'mncount' : mncount, 'dEUSD' : dailyEarningsUSD, 'dEBTC' : dailyEarningsBTC, 'dECOIN' : dailyEarningsCOIN, 'wEUSD' : weeklyEarningsUSD, 'wEBTC' : weeklyEarningsBTC, 'wECOIN' : weeklyEarningsCOIN, 'mEUSD' : monthlyEarningsUSD, 'mEBTC' : monthlyEarningsBTC, 'mECOIN' : monthlyEarningsCOIN, 'yEUSD' : yearlyEarningsUSD, 'yEBTC' : yearlyEarningsBTC, 'yCOIN' : yearlyEarningsCOIN, 'btcvalue' : btcvalue, 'scrivvalue' : scrivvalue, 'scrivbtcvol' : scrivbtcvol, 'scrivvol' : scrivvol, 'scrivusdvol' : scrivusdvol, 'scrivusdvalue' : scrivusdvalue}
    
await writeToJson(fileName, data)

		
		
		
