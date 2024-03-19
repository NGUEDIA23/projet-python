import platform
import subprocess
import os
import re
import argparse
 
def get_os():
    system = platform.system()
    if "Linux" in system:
        return "Linux"

    elif "Windows" in system:
        return "Windows"

    else:
        return "Error: Unknown OS"

def get_ip_configuration(system):
    conf = ""
    if "Linux" in system:
        try:
          result = subprocess.check_output(['ipconfig'],stderr=subprocess.STDOUT,universal_newlines=True)
          conf = result
        except subprocess.CalledProcessError as e:
            conf = f"Erreur lors de la recuperation de la configuration IP sur linux :{e.outpout}"
    elif "Windows" in system:
        try:
          result = subprocess.check_output(['ipconfig'],stderr=subprocess.STDOUT,universal_newlines=True)
          conf = result
        except subprocess.CalledProcessError as e:
            conf = f"Erreur lors de la recuperation de la configuration IP sur linux :{e.outpout}"
    else:
        conf = "Erreur : OS inconnu"
    # Effectuer la suite du programme
    
    return conf
    
if __name__ == "__main__":
    os = get_os()
    print(f"Nous sommes sur un système : {os}")
    ip_conf = get_ip_configuration(os)
    print(ip_conf)

    ip_found =False
    for line in ip_conf.splitlines():
        if "IPv4" in line:
            ip_found = True
            print("\033[91m" + line + "\033[0m")

        if not  ip_found:
            print("\033[91mIPv4 addresses not found .\033[0m")