import platform
import subprocess
import os
import re
import argparse

def retrieve_windoms_network_info():
    try:
        # verification de la plate forme 
        print("platform: Windows")

        #integre le fichier config
        with open("ipconfig_output.txt","w") as output_file:
            subprocess.run(["ipconfig"], stdout=output_file,text=True,check=True)
        
        #liste l'ensemble des fichiers
        directory = os.path.dirname(os.path.abspath("ipconfig_output.txt"))
        file_list = os.listdir(directory)
        print("Files in the directory:")
        for file in file_list:
            print(file)

        #lire le fichier config
        with open("ipconfig_output.txt", "r") as input_file:
            ipconfig_data = input_file.read()

        # IPV4 addresses 
        ip_addresses = [line.strip() for line in ipconfig_data.splitlines() if "IPv4 Address" in line]
        print("IPV4 Addresses:")
        for ip_address in ip_addresses:
            print(ip_address)

    except Exception as e:
        print(f"An error occured: {e}")

def retrieve_Linux_network_info():
    try:
        # Display platform information 
        print("platform: Linux")

        #Run 'ifconfig' and write the output to a file 
        with open("ipconfig_output.txt","w") as output_file:
            subprocess.run(["ifconfig"],stdout=output_file, text=True, check=True)
        
         #list files in the directory
        directory = os.path.dirname(os.path.abspath("ipconfig_output.txt"))
        file_list = os.listdir(directory)
        print("Files in the directory:")
        for file in file_list:
            print(file)

        #Read the created file
        with open("ifconfig_output.txt","r") as input_file:
            ifconfig_data = input_file.read()

        #Retrieve IPv4 addresses using regular expressions 
        ip_addresses = re.findall(r"inet(\d+\.\d+\.\d+\.\d+)", ifconfig_data)
        print( "IPv4 Addresses:")
        for ip_address in ip_addresses:
            print(ip_address)

    except Exception as e:
        print(f"An error occurred: {e}")
    
# Add command-line arguments
parser = argparse.ArgumentParser(description="script for retrieving network information")

#Add an  argument to display help
parser.add_argument("-a","--aide", action="store_true", help="Display help")

#Analyse the arguments
args = parser.parse_args()

if args.aide:
    parser.print_help()
else:
    #Chek the platform 
    system = platform.system()
    if system == "Windows":
        retrieve_windoms_network_info ()
    elif system == "Linux":
        retrieve_Linux_network_info()
    else:
        print(f"platform not supported: {system}")



