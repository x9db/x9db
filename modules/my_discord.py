import webbrowser
import os

os.system('cls' if os.name == 'nt' else 'clear')
os.system("color d")

print(f"""

▓█████▄     ██▓     ██████     ▄████▄      ▒█████      ██▀███     ▓█████▄    
▒██▀ ██▌   ▓██▒   ▒██    ▒    ▒██▀ ▀█     ▒██▒  ██▒   ▓██ ▒ ██▒   ▒██▀ ██▌   
░██   █▌   ▒██▒   ░ ▓██▄      ▒▓█    ▄    ▒██░  ██▒   ▓██ ░▄█ ▒   ░██   █▌   
░▓█▄   ▌   ░██░     ▒   ██▒   ▒▓▓▄ ▄██▒   ▒██   ██░   ▒██▀▀█▄     ░▓█▄   ▌   
░▒████▓    ░██░   ▒██████▒▒   ▒ ▓███▀ ░   ░ ████▓▒░   ░██▓ ▒██▒   ░▒████▓    
 ▒▒▓  ▒    ░▓     ▒ ▒▓▒ ▒ ░   ░ ░▒ ▒  ░   ░ ▒░▒░▒░    ░ ▒▓ ░▒▓░    ▒▒▓  ▒    
 ░ ▒  ▒     ▒ ░   ░ ░▒  ░ ░     ░  ▒        ░ ▒ ▒░      ░▒ ░ ▒░    ░ ▒  ▒    
 ░ ░  ░     ▒ ░   ░  ░  ░     ░           ░ ░ ░ ▒       ░░   ░     ░ ░  ░    
   ░        ░           ░     ░ ░             ░ ░        ░           ░       
 ░                            ░                                    ░                              
""")

url = "https://discord.gg/wldb"

webbrowser.open(url)

print(f"""
[1] Retourne au menu
""")

choice = int(input('\033[0;35m Choose >> '))

def execute_script(choice):
    if choice == 1:
        os.system('python main.py')

execute_script(choice)
