#!/bin/python
import os 
import sys
import time
import subprocess
from subprocess import call
#
#	nao esquece de me seguir manooo
#
ngrok = """
authtoken: 'chave'

tunnels:
  http_apache:
    proto: http
    addr: 80
  tcp_ssh:
    proto: tcp
    addr: 22
  tcp_demo:
    proto: tcp
    addr: 8000
"""
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
os.system('clear')
print('')
print('')
print(GREEN + """
      ooooo                           8 o    o                     8      
        8                             8 8b   8                     8      
        8   o    o odYo. odYo. .oPYo. 8 8`b  8 .oPYo. oPYo. .oPYo. 8  .o  
        8   8    8 8' `8 8' `8 8oooo8 8 8 `b 8 8    8 8  `' 8    8 8oP'   
        8   8    8 8   8 8   8 8.     8 8  `b8 8    8 8     8    8 8 `b.  
        8   `YooP' 8   8 8   8 `Yooo' 8 8   `8 `YooP8 8     `YooP' 8  `o. 
      ::..:::.....:..::....::..:.....:....:::..:....8 ..:::::.....:..::...
      :::::::::::::::::::::::::::::::::::::::::::ooP'.::::::::::::::::::::
      :::::::::::::::::::::::::::::::::::::::::::...::::::::::::::::::::::
"""+ RESET)
print(RED+"""
						Criado por SedSec
					
						https://instagram.com/fellipmg
						https://youtube.com/sedsec
						https://github.com/fellipmelo/
""")
print('')
print('')
time.sleep(5)
def start():
	auth = raw_input(' Sua Chave do NGROK: ')
	print('')
	art = ('ngrok')
	ngrok = ngrok.replace('chave', auth)
	arq = open('/root/.ngrok2/ngrok.yml', 'w')
	arq.write(ngrok)
	arq.close()
	porta = raw_input('Porta HTTP: ')
	tcp = raw_input('Porta TCP: ') 
	ngrok = ngrok.replace('80', porta)
	arq = open('/root/.ngrok2/ngrok.yml', 'w')
	arq.write(ngrok)
	arq.close()
	title = ('--all')
	ngrok = ngrok.replace('8000', tcp)
	arq = open('/root/.ngrok2/ngrok.yml', 'w')
	arq.write(ngrok)
	arq.close()
	print('')
	print('')
	print(GREEN+'Obrigado :)')
	time.sleep(3)
	execu = os.system(art+' start '+title)
	os.system(execu)
try:
	start()
exception Exception:
	pass
	start()


