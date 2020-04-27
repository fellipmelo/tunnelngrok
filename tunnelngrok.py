#!/bin/python3
#coding: utf-8

import os
from time import sleep


os.system('chmod 777 *')


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
    addr: 555
"""
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"
os.system('clear')
print('')
print('')

def banner():
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
    """ + RESET)
    print(RED + """
                            Criado por Fellip Melo      
                                                        Créditos: Equipe SedSec
                                                        https://www.youtube.com/sedsec
                            
                            https://instagram.com/fellipmg
                            https://www.youtube.com/channel/UC1cRedG4bvPdfPLpYNRYxJg
                            https://github.com/fellipmelo/
                            
                            
                            
    Para desinstalar:
    cd /etc/tunnelngrok/
    ./uninstall.sh
    """)
    print('')
    print('')
    sleep(15)
banner()
auth = input(' Sua Chave do NGROK: ')

print('')
# baixa ngrok
os.system('wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip')
# descompactar
try:
    os.system('unzip ngrok-stable-linux-amd64.zip')
    os.system('./ngrok authtoken ' + auth)
except:
    print(RED + """
    
    Extraia o Ngrok 
    Se der erro tente apagar os arquivos antigos do Ngrok e execute novamente.
    
    """)
art = ('./ngrok')
ngrok = ngrok.replace('chave', auth)
arq = open('/root/.ngrok2/ngrok.yml', 'w')
arq.write(ngrok)
arq.close()

os.system('clear')
banner()

porta = input('Porta HTTP: ')
print('')
tcp = input('Porta TCP: ')
ngrok = ngrok.replace('80', porta)
arq = open('/root/.ngrok2/ngrok.yml', 'w')
arq.write(ngrok)
arq.close()
title = ('--all')
ngrok = ngrok.replace('555', tcp)
arq = open('/root/.ngrok2/ngrok.yml', 'a')
arq.write(ngrok)
arq.close()

os.system('cp ngrok /bin')
os.system('mkdir /etc/tunnelngrok && cp * /etc/tunnelngrok && cp tn.py /bin/')

print('')
print('')
print(GREEN+"""     Obrigado :)

        Para chamar o Ngrok basta chamar no terminal: """ + RED + """tn.py""" + GREEN + """
        
        Para mudar alguma porta mais tarde basta desinstalar e executar novamente.

""")
sleep(10)

os.system('ngrok start --all')
