import argparse
import ipaddress
import subprocess
import test
def get_all_ip(ip_list):
    all_ips = []

    for item in ip_list:
        ip, subnet = item.split('/')
        network = ipaddress.IPv4Network(item, strict=False)
        
        for ip_addr in network.hosts():
            all_ips.append(str(ip_addr))

    return all_ips
    
def ping(ip):
    try:
        # Exécute la commande ping
        result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

        # Vérifie le code de retour
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False

def save_result(path, result):
    try:
        with open(path, 'w') as file:
            file.write(result)
        print(f"Le résultat a été sauvegardé dans le fichier {path}.")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde du résultat : {e}")

def choose_interface(ip_list):
     print("Liste des blocs d'IP disponibles :")
     for i, ip in enumerate(ip_list, 1):
        print(f"{i}. {ip}")

     while True:
        try:
            choice = int(input("Veuillez entrer le numéro du bloc d'IP à scanner : "))
            if 1 <= choice <= len(ip_list):
                return ip_list[choice - 1]
            else:
                print("Choix invalide. Veuillez entrer un numéro valide.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")

if __name__ == "__main__":
    os = test.get_os()
    ip_list = test.get_ip_configuration(os)    # Retourne la liste des ip des cartes réseaux de la machine
    ip_block = choose_interface(ip_list)  # L'utilisateur choisit son bloc d'ip
    list_ip = get_all_ip(ip_block)
    
    result = []
    for ip in list_ip:
        result.append(ping(ip))
        
    save_result("./result.txt", result)