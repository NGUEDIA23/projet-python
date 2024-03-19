import test
import platform
import subprocess
import tp1

def choose_network():
    networks = input("Entrez les réseaux que vous souhaitez scanner (séparés par des virgules): ").split(',')
    return [network.strip() for network in networks]

def scan_network(networks):
    online_ips = []
    for network in networks:
        for i in range(1, 255):
            ip = f"{network}.{i}"
            try:
                subprocess.check_output(['ping', '-c', '1', ip], stderr=subprocess.STDOUT, universal_newlines=True)
                online_ips.append(ip)
            except subprocess.CalledProcessError as e:
                pass  # Ignore les erreurs de ping
    
    return online_ips

def save_to_file(online_ips, filename="online_ips.txt"):
    with open(filename, 'w') as file:
        for ip in online_ips:
            file.write(ip + '\n')

if __name__ == "__main__":
    os_type = platform.system()
    print(f"Nous sommes sur un système : {os_type}")
    
    networks = choose_network()
    
    online_ips = scan_network(networks)
    
    if online_ips:
        print("Machines en ligne :")
        for ip in online_ips:
            print(ip)
        
        save_choice = input("Voulez-vous sauvegarder les adresses IP en ligne dans un fichier ? (oui/non): ").lower()
        
        if save_choice == "oui":
            save_to_file(online_ips)
            print("Adresses IP en ligne sauvegardées dans 'online_ips.txt'")
    else:
        print("Aucune machine en ligne trouvée.")
