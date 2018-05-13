from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import config
import json


def get_rpc():
    return AuthServiceProxy("http://%s:%s@%s:%s" % (
        config.rpc_config['rpc_username'], config.rpc_config['rpc_password'],
        config.rpc_config['rpc_host'],
        config.rpc_config['rpc_port']), timeout=config.rpc_config['timeout'])
		
def getMnInfoCRU():
    rpc = get_rpc()

    mncount = rpc.masternode('count')

    # let some daemon time to unlock wallet
    time.sleep(1)

	fileName = 'mncount'
	
	data = {}
	data['mncount'] = mncount
	writeToJson(path, fileName, data)

		
		
def writeToJson(path, fileName, data):
	filePathNameWExt = './' + path '/' + fileName + '.json'
	with open(filePathNameWExt, 'w') as fp;
		json.dump(data, fp)