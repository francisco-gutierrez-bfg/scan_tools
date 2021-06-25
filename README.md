                                                         Security Scanning
                                                         =================
                                                         


Importante:
===========

Esta herramienta se ha desarrollado para ejecutarse exclusivamente en dictribuciones Ubuntu 18.x en adelante.
Posiblemente correria en Debian, pero no ha sido probada.

Descripcion:
============
Sistema desarrollado para evaluar y ejecutar pentesting sobre sistemas informaticos con el fin de identificar puntos debiles,
esta herramienta no se ha desarrollado con fines delictivos.
El uso de los datos y los efectos que pueda causar su ejecucion son responsabilidad del usuario y no del desarrollador.
Esta herramienta se ha desarrollado con fines eticos y estrictamente para ejecucion de actividade de laboratorio.

Ejecucion:
==========
./security

Reportes de ejecucion:
======================
La ejecucion de esta utilidad hace registro de todo su actividad dentro en la siguientes ruta:
"Modules/REPORTES"


Componentes:
============

Esta utilidad consta de varios componentes, para lograr su fincionamiento.
 - Golang (go1.13.8 linux/amd64)
 - Python 3.5.x
 - Perl 5.x
 - Nmap
   - Nmap Scripts Vulners
   - Nmap Scripts Vulscan
 - Hydra
 - Bash
 - Git

Programa principal:
===================

El programa principal esta escrito en bash, contiene algunas funciones en perl y cumple las siguientes funciones:

1- Verificacion de todas las dependencias necearias para que las subrutinas (scripts Golang, Scripts NMAP).
   Sin estas dependencias, el programa no funciona, por esta razon, el programa principal dara inicio al 
   proceso de instaacion de dependencias automaticamente, pidiendo autorizacion y confirmacion del usuario.
   
   La instalacion de dependencias puede ser ejecutada manualmente de la siguiente manera:
   El script de instalacion de dependencias (install_dependencies) se encuentra ubicado en el folder denominado
   "Install_dependencies", para ejecutarlo solo es necesario correr el siguiente comando:
   ./install_dependencies       

2- Una vez las condiciones y dependencias son cumplidas, el programa principal presenta un menu con
   diferentes opciones para escaneo y explotacion de vulnerabilidades. 

Definicion de subrutinas:
=========================

Golang:
=======

Se encuentran ubicadas en el folder "Modules" y clasificadas de la siguiente manera:

HYDRA_GO: Contiene el codigo encargado de ejecutar tyareas de pentesting mediante
          procedimiento de fuerza bruta.
          Los diccionarios para dicho procedimiento se encuentran ubicados en el
          folder denominado con el mismo nombre "Diccionarios".

NIKTO_GO: Contiene el codigo de ejecucion de la herramienta de escaneo de vulnerabilidades
          en aplicaciones/portales web, en esta utilidad es necesario especificar el puerto
          en el que se ejecuta la aplicacion objetivo de la evaluacion.

NMAP_GO: Contiene codifgo de ejecucion de varias operaciones con NMAP, tales como:
         - Revision de CVE's
         - Revision de vulnerabilidades
         - Revision de puertos abiertos y disponibles. 

Bash:
=====
El programa principal se encuentra escrito en este interprete.

Perl:
=====
La barra de progreso se encuentra escrita en perl, esta barra se encarga de monitorear
el progreso de ejecuciones de algunas tareas de instalacion de dependencias.

Nmap:
=====
Herramienta con funcionalidades diversas enfocadas a la evaluacion de vulnerabilidades.

Nikto:
======
Herramienta con funcionalidades diversas enfocadas a la evaluacion de vulnerabilidades
en aplicaciones web.

Hydra:
======
Herramienta con funcionalidades de crackeo de credenciales enfocada a la penetracion
de diersos sistemas informaticos y/o de comunicaciones mediante mecanismos de
fuerza bruta.


Desarrollado por:
 Francisco Javier Gutierrez G.
 Sr Linux Engineer
 fgutierrez@hexacta.com
 HEXACTA 2021

