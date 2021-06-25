#!/usr/bin/env python3

# -*- coding: utf-8 -*-
#title           :security.py
#description     :Escaneo de Vulnerabilidades y Pentesting
#author          :Francisco Gutierrez
#date            :
#version         :1
#usage           :python security.py
#notes           :
#python_version  :3.x.x 
#=======================================================================

# Import the modules needed to run the script.
import sys, os

# Main definition - constants
menu_actions  = {}  

#os.chdir('Modules/NMAP_GO')
#print(os.getcwd())

# ========================
#     Funcion de Menu
# ========================

# Main menu
def main_menu():
    os.system('clear')
    
    print ("Escaneo de vulnerabilidades y pentesting\n")
    print ("########################################")
    print ("1. Escaneo y chequeo de CVE's")
    print ("2. Escaneo de vulnerabilidades con NMAP")
    print ("3. Escaneo de vulnerabilidades web con NIKTO")
    print ("4. Escaneo y verificacion de puertos abiertos")
    print ("5. Pentestting con Hydra")
    print ("\n0. Salir")
    choice = input(" >>  ")
    exec_menu(choice)

    return

# Ejecucion de Menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("Opcion invalida.\n")
            menu_actions['main_menu']()
    return

# Opcion 1
def menu1():
    print ("Escaneo y chequeo de CVE's\n")
    print ("##########################")
    ip = input("Ingrese IP de dispositivo:")
    os.system('nmap -Pn --script vuln ' + ip)
    input("Presione Enter para continuar...")
    back()
    return


# Opcion 2 2
def menu2():
    print ("Escaneo de Vulnerabilidades\n")
    print ("###########################")
    ip = input("Ingrese IP de dispositivo:")
    os.system('nmap -sV --script=nmap-vulners ' + ip)
    input("Presione Enter para continuar...")
    back()
    return

# Opcion 3
def menu3():
    print ("Escaneo de Vulnerabilidades de sitios web\n")
    print ("#########################################")
    ip = input("Ingrese IP de dispositivo:")
    puerto = input("Ingrese puerto de sitio web:")
    command = "nikto -host %s -port %s" % (ip, puerto)
    os.system(command)
    input("Presione Enter para continuar...")
    back()
    return

# Opcion 4
def menu4():
    print ("Escaneo e identificacion de puertos abiertos\n")
    print ("###########################")
    ip = input("Ingrese IP de dispositivo:")
    os.system('nmap ' + ip)
    input("Presione Enter para continuar...")
    back()
    return

# Opcion 5
def menu5():
    print ("Pentesting\n")
    print ("##########")
    print("")
    print ("   ##################################################################################################################")
    print ("   #  Este proceso puede tardar un tiempo, posiblemente horas, presione <Enter> para continuar, si esta de acuerdo  #")
    print ("   ##################################################################################################################")
    input("")
    print("")
    ip = input("Ingrese IP de dispositivo:")
    puerto = input("Ingrese nombre servicio, ejemplo: rdp,ssh,ftp,telnet:")
    puertonum = input("Ingrese numero de puerto:")
    print("")
    print("Trying Nmap bruteforce...")
    command1 = "nmap -p %s --script %s-brute --script-args userdb=Modules/HYDRA_GO/diccionarios/wordlists/users.lst,passdb=Modules/HYDRA_GO/diccionarios/wordlists/passwords.lst %s" % (puertonum, puerto, ip)
    os.system(command1)
    print("")
    print("Trying Hydra...")
    command = "hydra -L Modules/HYDRA_GO/diccionarios/wordlists/users.lst -P Modules/HYDRA_GO/diccionarios/wordlists/passwords.lst %s %s | grep -vi github | grep -vi warning" % (ip, puerto)
    os.system(command)
    print("")
    input("Presione Enter para continuar...")
    back()
    return


# Back to main menu
def back():
    menu_actions['main_menu']()

# Exit program
def exit():
    sys.exit()

# ========================
#    Definicion de Menu
# ========================

# Menu definition
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
#     Programa P/pal
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
