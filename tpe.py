
import os

def get_os():
   
    if "Linux" in os.uname():
        return "Linux"
    elif "Windows" in os.uname():
        return "Windows"
    else:
        return "Inconnu"

def get_ip_configuration(system):
    conf = ""
    if "Linux" in system:
        # Récupérer la configuration IP pour Linux
         conf = ""
    elif "Windows" in system:
         # Récupérer la configuration IP pour Windows
         conf = ""
    else:
        conf = "Erreur : OS inconnu"
    
    # Effectuer la suite du programme
    
    return conf
    
if __name__ == "__main__":
    os = get_os()
    print(f"Nous sommes sur un système : {os}")
    ip_conf = get_ip_configuration(os)
    print(ip_conf)