import os, socket
from colorama import Fore, Style, init

init(autoreset=True)

class color:
    RED = Fore.RED + Style.BRIGHT
    WHITE = Fore.WHITE + Style.BRIGHT
    RESET = Fore.RESET + Style.RESET_ALL

hostname = socket.gethostname()
host = socket.gethostbyname(hostname)

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def scan_ip(ip): 
    print(color.WHITE + '[*] Scanne en cours...\n')
    for port in range(65535):   
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv.settimeout(1)
        try:
            serv.connect((ip, port))
            print(color.RED + f'[OPEN]: Port {port} -->  [{ip}:{port}]' + color.RESET)
        except:
            pass
        finally:
            serv.close() 

def main():
    while True:
        clear()
        title = f'''
                                                                                                                      

  ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  
▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
  ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░ 
      ░  ░ ░            ░  ░         ░          ░    ░  ░   ░     
         ░                                                        
                                                                                                                      
                        [Made by X9DB] 
'''
        print(color.WHITE + title)

        ip = input(color.WHITE + '[+] Enter the IP to scan: ' + color.RED)
        scan_ip(ip)

        choice = input(color.WHITE + '[*] Press ENTER to return the menu or type "exit" to quit: ')
        if choice.lower() == "exit":
            break

if __name__ == "__main__":
    main()
