# Modules à installer en faisant le setup
import os
import base64
from tkinter.filedialog import Open
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init


tool=Fore.WHITE +"""
 ██▓▓█████▄    ▄▄▄█████▓ ▒█████     ▄▄▄█████▓ ▒█████   ██ ▄█▀▓█████  ███▄    █ 
▓██▒▒██▀ ██▌   ▓  ██▒ ▓▒▒██▒  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▓█   ▀  ██ ▀█   █ 
▒██▒░██   █▌   ▒ ▓██░ ▒░▒██░  ██▒   ▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒███   ▓██  ▀█ ██▒
░██░░▓█▄   ▌   ░ ▓██▓ ░ ▒██   ██░   ░ ▓██▓ ░ ▒██   ██░▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒
░██░░▒████▓      ▒██▒ ░ ░ ████▓▒░     ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░▒████▒▒██░   ▓██░
░▓   ▒▒▓  ▒      ▒ ░░   ░ ▒░▒░▒░      ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒ 
 ▒ ░ ░ ▒  ▒        ░      ░ ▒ ▒░        ░      ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░
 ▒ ░ ░ ░  ░      ░      ░ ░ ░ ▒       ░      ░ ░ ░ ▒  ░ ░░ ░    ░      ░   ░ ░ 
 ░     ░                    ░ ░                  ░ ░  ░  ░      ░  ░         ░ 

  [+] Made by x9db
                                                                                                   
""" + Fore.BLUE
print(tool)
init()

userid = input("ID de ta victime : ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n  Moitié du token : {encodedStr}')
print(' ')
os.system('pause >nul')
