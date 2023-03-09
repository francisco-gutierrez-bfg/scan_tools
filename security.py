#!/usr/bin/env python3

# -*- coding: utf-8 -*-
#Title           :security.py
#description     :Vulnerability Scanning and Pentesting
#author          :Francisco Gutiérrez
#date            :Jun 25 2021
#version         :1
#usage           :python security.py or python3 security.py if you don´t have your environment var set.
#python_version  :3.x.x 
#======================================================================================================

import sys, os

menu_actions  = {}  

#os.chdir('Modules/NMAP_GO')
#print(os.getcwd())

# ========================
#         Menu
# ========================

# Main Menu
def main_menu():
    os.system('clear')
    
    print ("Vulnerability scan and pentesting\n")
    print ("#################################")
    print ("1. Check for CVE's")
    print ("2. Vulnerability scan with NMAP")
    print ("3. Web vulnerability scan with NIKTO")
    print ("4. Open ports validation")
    print ("5. Pentesting with Hydra and Nmap")
    print ("\n0. Exit")
    choice = input(" >>  ")
    exec_menu(choice)

    return

# Main menu execution
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("Inválid Option.\n")
            menu_actions['main_menu']()
    return

# Opción 1
def menu1():
    print ("Check for CVE's\n")
    print ("###############")
    ip = input("Type a device IP:")
    os.system('sudo  -Pn --script vuln ' + ip)
    input("Press Enter to continue...")
    back()
    return


# Opción 2
def menu2():
    print ("Vulnerability scan with NMAP\n")
    print ("############################")
    ip = input("Type a device IP:")
    os.system('sudo nmap -sV --script=nmap-vulners ' + ip)
    input("Press Enter to continue...")
    back()
    return

# Opción 3
def menu3():
    print ("Web sites vulnerability scan with NIKTO\n")
    print ("#######################################")
    ip = input("Type a device IP:")
    puerto = input("Type a web site/app URL:")
    command = "sudo nikto -host %s -port %s" % (ip, puerto)
    os.system(command)
    input("Press Enter to continue...")
    back()
    return

# Opción 4
def menu4():
    print ("Open ports validation\n")
    print ("#####################")
    ip = input(Type a device IP:")
    os.system('sudo nmap ' + ip)
    input("Press Enter to continue...")
    back()
    return

# Opción 5
def menu5():
    print ("Pentesting\n")
    print ("##########")
    print("")
    print ("   ##################################################################################################################")
    print ("   #         This procedure can take more than usual, maybe hours, press <Enter> to continue if you agree.          #")
    print ("   ##################################################################################################################")
    input("")
    print("")
    ip = input("Type a device IP:")
    puerto = input("type a service name, Ex: rdp,ssh,ftp,telnet:")
    puertonum = input("Type port number:")
    print("")
    print("Trying brute force using Nmap...")
    command1 = "sudo nmap -p %s --script %s-brute --script-args userdb=Modules/HYDRA_GO/diccionarios/wordlists/users.lst,passdb=Modules/HYDRA_GO/diccionarios/wordlists/passwords.lst %s" % (puertonum, puerto, ip)
    os.system(command1)
    print("")
    print("Trying brute force using Hydra...")
    command = "sudo hydra -L Modules/HYDRA_GO/diccionarios/wordlists/users.lst -P Modules/HYDRA_GO/diccionarios/wordlists/passwords.lst %s %s | grep -vi github | grep -vi warning" % (ip, puerto)
    os.system(command)
    print("")
    input("Press Enter to continue...")
    back()
    return


# Back to main menu
def back():
    menu_actions['main_menu']()

def exit():
    sys.exit()

# ========================
#   Main Menu Definition
# ========================

menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '3': menu3,
    '4': menu4,
    '5': menu5,
    '0': exit,
}

# =======================
#      Main Program
# =======================

if __name__ == "__main__":
    # Launch main menu
    main_menu()
