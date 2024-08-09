import re
import socket
import uuid
import subprocess
import platform
import os

os.system('color D')
os.system('cls' if os.name == 'nt' else 'clear')

print(f"""
                    ██▓███   ▄████▄      ██▓ ███▄    █   █████▒▒█████  
                    ▓██░  ██▒▒██▀ ▀█     ▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
                    ▓██░ ██▓▒▒▓█    ▄    ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
                    ▒██▄█▓▒ ▒▒▓▓▄ ▄██▒   ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
                    ▒██▒ ░  ░▒ ▓███▀ ░   ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
                    ▒▓▒░ ░  ░░ ░▒ ▒  ░   ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ 
                    ░▒ ░       ░  ▒       ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ 
                    ░░       ░            ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  
                             ░ ░          ░           ░            ░ ░  


Made by X9DB
""")

class PCInfo:
    def __init__(self):
        self.IP = input("Entrez l'adresse IP de votre cible >>> ")
        while not self.validate_ip(self.IP):
            print("Adresse IP invalide. Veuillez réessayer.")
            self.IP = input("Entrez l'adresse IP de votre cible : ")

    def validate_ip(self, ip):
        pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        return pattern.match(ip) is not None

    def get_username(self):
        return os.getenv("USERNAME") or os.getenv("USER")

    def get_pc_name(self):
        return socket.gethostname()

    def get_mac_address(self):
        mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        return mac

    def get_ip_addresses(self):
        ipv4 = socket.gethostbyname(socket.gethostname())
        ipv6 = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET6)
        ipv6 = [addr[4][0] for addr in ipv6 if addr[1] == socket.SOCK_STREAM]
        return ipv4, ipv6[0] if ipv6 else None

    def get_uuid(self):
        if platform.system() == "Windows":
            command = "wmic csproduct get uuid"
            uuid_str = subprocess.check_output(command, shell=True).decode().split("\n")[1].strip()
        else:
            uuid_str = subprocess.check_output('cat /proc/sys/kernel/random/uuid', shell=True).decode().strip()
        return uuid_str

    def display_info(self):
        print(f"Nom d'utilisateur : {self.get_username()}")
        print(f"Nom du PC : {self.get_pc_name()}")
        print(f"Adresse MAC : {self.get_mac_address()}")
        ipv4, ipv6 = self.get_ip_addresses()
        print(f"Adresse IPv4 : {ipv4}")
        print(f"Adresse IPv6 : {ipv6}")
        print(f"UUID du PC : {self.get_uuid()}")
        print(f"""
        [1] back to menu
        """)
        choice = int(input('\033[0;35m Choose >>> '))
        def execute_script(choice):
            if choice == 1:
                os.system('python main.py')
            elif choice == 2:
                os.system('python whois_lookup.py')

        execute_script(choice)


if __name__ == "__main__":
    pc = PCInfo()
    pc.display_info()
