from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import config
import json


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
	
	
	data = {}
	data['mncount'] = mncount
	data['dEUSD'] = dailyEarningsUSD, data['dEBTC'] = dailyEarningsBTC, data['dECOIN'] = dailyEarningsCOIN
	data['wEUSD'] = weeklyEarningsUSD, data['wEBTC'] = weeklyEarningsBTC, data['wECOIN'] = weeklyEarningsCOIN
	data['mEUSD'] = monthlyEarningsUSD, data['mEBTC'] = monthlyEarningsBTC, data['mECOIN'] = monthlyEarningsCOIN
	data['yEUSD'] = yearlyEarningsUSD, data['yEBTC'] = yearlyEarningsBTC, data['yCOIN'] = yearlyEarningsCOIN
	writeToJson(path, fileName, data)

		
		
def writeToJson(path, fileName, data):
	filePathNameWExt = './' + path '/' + fileName + '.json'
	with open(filePathNameWExt, 'w') as fp;
		json.dump(data, fp)