from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import config
import json
import asyncio
import requests

def get_rpc():
    return AuthServiceProxy("http://%s:%s@%s:%s" % (
        config.rpc_config['rpc_username'], config.rpc_config['rpc_password'],
        config.rpc_config['rpc_host'],
        config.rpc_config['rpc_port']), timeout=config.rpc_config['timeout'])
		
def getInfoCRU():
    rpc = get_rpc()

    mncount = rpc.masternode('count')

    # let some daemon time to unlock wallet
    time.sleep(1)

    fileName = 'mncount'
    dailyEarningsUSD = (((blocksPerADay * mncount) * blockRewardForMasternodes) * costinbtc * usdValueBtc)
    dailyEarningsBTC = (((blocksPerADay * mncount) * blockRewardForMasternodes) * costinbtc)
    dailyEarningsCOIN = (((blocksPerADay * mncount) * blockRewardForMasternodes)
	
    weeklyEarningsUSD = dailyEarningsUSD * 7 
    weeklyEarningsBTC = dailyEarningsBTC  * 7
    weeklyEarningsCOIN = dailyEarningsCOIN * 7
	
    monthlyEarningsUSD = weeklyEarningsUSD * 4
    monthlyEarningsBTC = weeklyEarningsBTC * 4
    monthlyEarningsCOIN = weeklyEarningsCOIN * 4
	
    yearlyEarningsUSD = dailyEarningsUSD * 365
    yearlyEarningsBTC = dailyEarningsBTC * 365
    yearlyEarningsCOIN = dailyEarningsCOIN * 365
	
    fileName = config.coinName['coin']
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
	
    data = {}
    data['mncount'] = mncount
    data['dEUSD'] = dailyEarningsUSD, data['dEBTC'] = dailyEarningsBTC, data['dECOIN'] = dailyEarningsCOIN
    data['wEUSD'] = weeklyEarningsUSD, data['wEBTC'] = weeklyEarningsBTC, data['wECOIN'] = weeklyEarningsCOIN
    data['mEUSD'] = monthlyEarningsUSD, data['mEBTC'] = monthlyEarningsBTC, data['mECOIN'] = monthlyEarningsCOIN
    data['yEUSD'] = yearlyEarningsUSD, data['yEBTC'] = yearlyEarningsBTC, data['yCOIN'] = yearlyEarningsCOIN
	
    data['btcvalue'] = btcvalue, data['scrivvalue'] = scrivvalue, data['scrivbtcvol'] = scrivbtcvol
    data['scrivvol'] = scrivvol, data['scrivusdvol'] = scrivusdvol, data['scrivusdvalue'] = scrivusdvalue

    writeToJson(path, fileName, data)

		
		
def writeToJson(path, fileName, data):
	filePathNameWExt = './' + path '/' + fileName + '.json'
	with open(filePathNameWExt, 'w') as fp;
		json.dump(data, fp)
