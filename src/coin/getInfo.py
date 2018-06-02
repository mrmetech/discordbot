from subprocess import Popen
import time		

while True:		

	time.sleep(600)
	Popen('python3 curium/coinInfo.py')
	Popen('python3 gravium/coinInfo.py')
	Popen('python3 scriv/coinInfo.py')
	Popen('python3 phore/coinInfo.py')
