from subprocess import Popen
import time		

while True:		

	Popen(['python3', 'curium/coinInfo.py'])
	Popen(['python3', 'gravium/coinInfo.py'])
	Popen(['python3', 'scriv/coinInfo.py'])
	Popen(['python3', 'phore/coinInfo.py'])
	time.sleep(600)
