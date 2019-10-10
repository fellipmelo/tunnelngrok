#!/bin/python
import os 
import sys
import time
import subprocess
from subprocess import call
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
   __                              __                              __  
  / /_ __  __ ____   ____   ___   / /  ____   ____ _ _____ ____   / /__
 / __// / / // __ \ / __ \ / _ \ / /  / __ \ / __ `// ___// __ \ / //_/
/ /_ / /_/ // / / // / / //  __// /  / / / // /_/ // /   / /_/ // ,<   
\__/ \__,_//_/ /_//_/ /_/ \___//_/  /_/ /_/ \__, //_/    \____//_/|_|  
                                           /____/                      

"""+ RESET)
print(RED+"""
						Criado por SedSec
					
						https://instagram.com/sedsec
""")
print('')
print('')
time.sleep(3)
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



