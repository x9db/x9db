import os
from os import system

title="X9DB TOOLS | made by x9db "
system("title "+title)

os.system('color D')
os.system('cls' if os.name == 'nt' else 'clear')


menu = """
                    ██╗  ██╗ █████╗ ██████╗ ██████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗
                    ╚██╗██╔╝██╔══██╗██╔══██╗██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
                     ╚███╔╝ ╚██████║██║  ██║██████╔╝       ██║   ██║   ██║██║   ██║██║     ███████╗
                     ██╔██╗  ╚═══██║██║  ██║██╔══██╗       ██║   ██║   ██║██║   ██║██║     ╚════██║
                    ██╔╝ ██╗ █████╔╝██████╔╝██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
                    ╚═╝  ╚═╝ ╚════╝ ╚═════╝ ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                          
                                                  ╔══════════════╗
                                                  ║ Made by x9db ║
                                                  ║ version 1.0  ║
                                                  ╚═══════╦══════╝
                                                          ║
                                        ╔═════════════════╩════════════════╗
                                        ║          X9DB TOOLS              ║
                                        ║   https://discord.gg/RjfHthDdGG  ║
                                        ║         discord.gg/wldb          ║
                                        ║                                  ║
                                        ╚═════════════════╦════════════════╝
                                                          ║
                               ╔══════════════════════════╩════════════════════════╗
                               ║                                                   ║                              
        ╔══════════════════════╩════════════════════════╗ ╔════════════════════════╩══════════════════════╗ 
        ║   [1] > Tool info                             ║ ║   [11] > Webhook spammer                      ║
        ║   [2] > Ip tools                              ║ ║   [12] > Scan IP                              ║
        ║   [3] > Whois lookup                          ║ ║   [13] > Id To First part Token               ║
        ║   [4] > OSINT Framework (website)             ║ ║   [14] > Account Disabler                     ║ 
        ║   [5] > IP pinger                             ║ ║   [15] > Gen Nitro                            ║
        ║   [6] > PC Info                               ║ ║   [16] > Temp Mail (website)                  ║
        ║   [7] > Discord token info                    ║ ║   [17] > Soon                                 ║ 
        ║   [8] > Username Tracker                      ║ ║   [17] > Soon                                 ║
        ║   [9] > Linkvertise Bypasser                  ║ ║   [18] > Soon                                 ║                         
        ║   [10]> Discord server info                   ║ ║   [19] > Discord du créateur                  ║
        ╚═══════════════════════════════════════════════╝ ╚═══════════════════════════════════════════════╝      
"""
print(menu)

choice = int(input('╚══root@ '))

def execute_script(choice):
    if choice == 1:
        os.system('python ./modules/tool_info.py')
    elif choice == 2:
        os.system('python ./modules/ip_lookup.py')
    elif choice == 3:
        os.system('python ./modules/whois_lookup.py')
    elif choice == 4:
        os.system('python ./modules/osint_tool.py')
    elif choice == 5:
        os.system('python ./modules/IP-Pinger.py')
    elif choice == 6:
        os.system('python ./modules/PC_info.py')
    elif choice == 7:
        os.system('python ./modules/discord_token_info.py')
    elif choice == 8:
        os.system('python ./modules/username_tracker.py')
    elif choice == 9:
        os.system('python ./modules/linkvertise_bypasser.py')
    elif choice == 10:
        os.system('python ./modules/discord_server_info.py')
    elif choice == 11:
        os.system('python ./modules/webhspam.py')
    elif choice == 12:
        os.system('python ./modules/scanner.py')
    elif choice == 13:
        os.system('python ./modules/ID_To_First_Part_Token.py')
    elif choice == 14:
        os.system('python ./modules/accountdisabler.py')
    elif choice == 15:
        os.system('python ./modules/nitro.py')
    elif choice == 19:
        os.system('python ./modules/my_discord.py')
    elif choice == 16:
        os.system('python ./modules/temp_mail.py')
execute_script(choice)
