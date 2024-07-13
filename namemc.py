import math
from subprocess import call
import sys
import os
from sys import platform
import asyncio
import requests
from termcolor import colored
from colorama import init
from fake_useragent import UserAgent
from pystyle import Colorate, Colors
import time

ua = UserAgent()

init()

sys.stdout.write("\x1b]2;ViewBot | TrentaSei 👽\x07")

def clear():
    command = 'cls' if platform in ('win32', 'cygwin') else 'clear'
    try:
        call(command, shell=True)
    except OSError as e:
        pass

async def view(username, number=None, proxies=None, headers=None, timeout=None):
    url = f"https://namemc.com/profile/{username}" + (f".{number}" if number else "")
    r = requests.get(url, headers=headers, proxies=proxies, timeout=timeout)
    return r.status_code

def print_banner():
    clear()
    print(Colorate.Vertical(Colors.purple_to_blue, '''
    
 ███▄    █  ▄▄▄       ███▄ ▄███▓▓█████  ███▄ ▄███▓ ▄████▄      ██▒   █▓ ██▓▓█████  █     █░ ▄▄▄▄    ▒█████  ▄▄▄█████▓
 ██ ▀█   █ ▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ ▓██▒▀█▀ ██▒▒██▀ ▀█     ▓██░   █▒▓██▒▓█   ▀ ▓█░ █ ░█░▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
▓██  ▀█ ██▒▒██  ▀█▄  ▓██    ▓██░▒███   ▓██    ▓██░▒▓█    ▄     ▓██  █▒░▒██▒▒███   ▒█░ █ ░█ ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ ▒██    ▒██ ▒▓▓▄ ▄██▒     ▒██ █░░░██░▒▓█  ▄ ░█░ █ ░█ ▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
▒██░   ▓██░ ▓█   ▓██▒▒██▒   ░██▒░▒████▒▒██▒   ░██▒▒ ▓███▀ ░      ▒▀█░  ░██░░▒████▒░░██▒██▓ ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░░ ▒░   ░  ░░ ░▒ ▒  ░      ░ ▐░  ░▓  ░░ ▒░ ░░ ▓░▒ ▒  ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
░ ░░   ░ ▒░  ▒   ▒▒ ░░  ░      ░ ░ ░  ░░  ░      ░  ░  ▒         ░ ░░   ▒ ░ ░ ░  ░  ▒ ░ ░  ░▒   ░   ░ ▒ ▒░     ░    
   ░   ░ ░   ░   ▒   ░      ░      ░   ░      ░   ░                ░░   ▒ ░   ░     ░   ░   ░    ░ ░ ░ ░ ▒    ░      
         ░       ░  ░       ░      ░  ░       ░   ░ ░               ░   ░     ░  ░    ░     ░          ░ ░           
                                                  ░                ░                             ░                   
                                                   by TrentaSei | V1.0
    '''))

while True:
    try:
        print_banner()

        username = input(f"[{colored('?', 'red')}] Username: ").strip()
        if not username:
            continue

        usernumber = input(f"[{colored('?', 'red')}] User number in case needed: ").strip() or None
        
        repeat_count = int(input(f"[{colored('?', 'red')}] How many times to repeat the process? (default 1): ") or 1)
        print()

        proxy_host = ''
        proxy_port = 823
        proxy_login = ''
        proxy_password = ''
        proxy = f'http://{proxy_login}:{proxy_password}@{proxy_host}:{proxy_port}'

        sviews = 0

        for _ in range(repeat_count):
            headers = {'user-agent': ua.random}
            r_status_code = asyncio.run(view(username=username, number=usernumber, proxies={"https": proxy}, headers=headers, timeout=10))

            if r_status_code == 403:
                sviews += 1
                print(f"[{colored('+' + str(sviews), 'green')}]", f"{colored('times viewed', 'white')}")
            elif r_status_code == 404:
                print(colored("No such profile", "red"))
                exit()
            else:
                print(colored(f"Sent a request and got status code {r_status_code}", "magenta"))

        time.sleep(2)
        print()
        print(colored("Refreshing in 5 seconds", "yellow"), end='', flush=True)
        for i in range(5):
            time.sleep(1)
            print(colored(".", "yellow"), end='', flush=True)
        print()

    except KeyboardInterrupt:
        print(colored("Bye!", "green"))
        exit()

    except Exception as e:
        print(f"{e}\n{colored('Error has occurred! ^')}")