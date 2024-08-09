import os
import colorama
import threading
import requests
import sys,os
from colorama import Fore
colorama.init()
 
#x9db


os.system('cls')

print("\037")


def dos(target):
    while True:
        try:
            res = requests.get(target)
            print("Request sent!")
        except requests.exceptions.ConnectionError:
            print("[!!!] " + "Connexion interrompue!")
 
threads = 20

print(Fore.BLUE+"""
 ██▓███   ██▓ ███▄    █   ▄████ ▓█████  ██▀███  
▓██░  ██▒▓██▒ ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▒██▒▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒░██░▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░░██░▒██░   ▓██░░▒▓███▀▒░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░░▓  ░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░      ▒ ░░ ░░   ░ ▒░  ░   ░  ░ ░  ░  ░▒ ░ ▒░
░░        ▒ ░   ░   ░ ░ ░ ░   ░    ░     ░░   ░ 
          ░           ░       ░    ░  ░   ░     
                                                
                                                
""")

print('-' * 60)

print('Par x9db')
print('-' * 60)


ip_to_check = input('Veuillez mettre une adresse IP à ping : ')

print('-' * 60)
os.system('ping -n 10000 {}'.format(ip_to_check))
print('-' * 60)

input('Appuyez sur Entrée pour quitter..')
