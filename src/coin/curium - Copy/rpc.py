from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import config
import json

def get_rpc():
    return AuthServiceProxy("http://%s:%s@%s:%s" % (
        config.rpc_config['rpc_username'], config.rpc_config['rpc_password'],
        config.rpc_config['rpc_host'],
        config.rpc_config['rpc_port']), timeout=config.rpc_config['timeout'])
def writeToJson(path, fileName, data):
	filePathNameWExt = '../../coinData/' + fileName + '.json'
	with open(filePathNameWExt, 'w') as fp:
		json.dump(data, fp, indent=4)
