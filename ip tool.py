import socket
import json
import os
from requests import get



ED      = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'

print(f''' 
{YELLOW}
 ▪   ▄▄▄·  ▄▄▄▄▄            ▄▄▌  
██ ▐█ ▄█  •██   ▄█▀▄  ▄█▀▄ ██•  
▐█· ██▀·   ▐█.▪▐█▌.▐▌▐█▌.▐▌██▪  
▐█▌▐█▪·•   ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌
▀▀▀.▀      ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀ {RESET}{BLUE}
                                  / \------------------, 
                                 \_,|                 | 
                                    |    By NOT YOU   | 
                                    |  ,----------------
                                    \_/_______________/                                                                    
                                {RESET}''')

def hip ():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    print(host)
    print(ip)

def frip ():
    url = 'http://ipinfo.io/json'
    response = get(url)
    data = json.loads(response.text)

    city = data['city']
    region = data['region']
    country = data['country']
    postal = data['postal']
    timezone = data['timezone']
    ip = data['ip']

    print("ip:", ip)
    print("city:", city)
    print("region:", region),
    print("country:", country)
    print("postal:", postal)
    print("timezone", timezone)

def gok():
    url = input('link : ')
    ip = socket.gethostbyname(url)
    print(ip)

def bou():
    print(f'''
    {MAGENTA}
         
         ░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░
         ░░░░███░█░░█████░█████░█░░░░░░█░░░░░░░░░
         ░░░░█░█░█░░█░░░█░░░█░░░░█░░░░░█░░░░░░░░░
         ░░░░█░███░░█░░░█░░░█░░░░██░░░█░░░░░░░░░░
         ░░░░█░░██░░█░░░█░░░█░░░░░█░░██░░░░░░░░░░
         ░░░░█░░░█░░█████░░░█░░░░░█░██░░░░░░░░░░░
         ░░░░░░░░░░░░░░░░░░░░░░░░░███░░░░░░░░░░░░
         ░░░░░░░░░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░
         ░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░
         ░░░░░░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░░
         ░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░
         ░░░░░░░░░░░░░░░████░░░░████░░██░██░░░░░░
         ░░░░░░░░░░░█████░░░░░░██░░░█░██░██░░░░░░
         ░░░░░░░░░██░░░░░░░░░░░░█████░█████░░░░░░
    {RESET}
    {CYAN}
         [+] Github : https://github.com/Yoydhb530/PYTHON-IP-TOOL-.git
         [+] discord : https://discord.gg/hcansqryZr   
    {RESET}                            
   ''')


print('''
    [1] link to ip
    [2] my ip address & host name 
    [3] my ifo-ip address
    [4] about
''')



linp = input("select number : ")

if linp == '1' :
    gok()
if linp == '2' :
    hip()

if linp == '3':
    frip()
if linp == '4':
    bou()