import argparse, os, socket
import tp1, tp2 

def ping_scan():
    """
    Réalise un scan avec ping sur un bloc d'ip choisit par l'utilisateur.
    """
    os = tp1.get_os()
    ip_list = tp1.get_ip_configuration(os)    # Retourne la liste des ip des cartes réseaux de la machine
    ip_block = tp2.choose_interface(ip_list)  # L'utilisateur choisit son bloc d'ip
    list_ip = tp2.get_all_ip(ip_block)
    
    result = []
    for ip in list_ip:
        result.append(ping(ip))
        
    return result

def socket_scan(list_port):
    """
    1. Réaliser un scan réseau avec ping_scan sur la carte réseau choisit de l'utilisateur.
    2. Effectuer un scan de port avec Socket SANS NMAP à partir des ip disponibles relevées par le scan précédent.
    """
    
    ip_list = ping_scan()
    
    result = ""
    for ip in ip_list:
        # Faire le scan de port sur l'ip
        result = "LE RESULTAT"
        
    return result

if __name__ == "__main__":
    params = "PARAMETRE A RECUPERER ET A TRAITER AVEC ARGPARSE"
    
    # if params == "-p":
    result = ping_scan()
    # elif params == "-s":
    result = socket_scan()
    
    #if params == "-o"
    tp2.save_result("./result-scan-tp3.txt", result)
    #sinon
    print(result)