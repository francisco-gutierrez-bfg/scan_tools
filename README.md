                                                         Security Scanning
                                                         =================
                                                         


Importante:
===========

Esta herramienta se ha desarrollado para ejecutarse exclusivamente en dictribuciones Ubuntu 18.x en adelante.
Posiblemente correría en Debian, pero no ha sido probada.

Descripción:
============
Sistema desarrollado para evaluar y ejecutar pentesting sobre sistemas informáticos con el fin de identificar puntos débiles,
esta herramienta no se ha desarrollado con fines delictivos.
El uso de los datos y los efectos que pueda causar su ejecución son responsabilidad del usuario y no del desarrollador.
Esta herramienta se ha desarrollado con fines éticos y estrictamente para ejecución de actividades de laboratorio.

Ejecución:
==========
./security

Reportes de ejecucion:
======================
La ejecucion de esta utilidad hace registro de todo su actividad dentro en la siguientes ruta:
"Modules/REPORTES"


Componentes:
============

Esta utilidad consta de varios componentes, para lograr su funcionamiento debe tener en cuenta las siguientes dependencias:
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

El programa principal está escrito en bash, contiene algunas funciones en perl y cumple las siguientes funciones:

1- Verificación de todas las dependencias necearias para el correcto funcionamiento de las subrutinas
   (Scripts Golang, Scripts NMAP).
   Sin estas dependencias, la solución no funcionará, por esta razón el programa principal dará inicio al 
   proceso de instalación de dependencias automáticamente, pidiendo autorización y confirmación del usuario.
   
   La instalación de dependencias puede ser ejecutada manualmente de la siguiente manera:
   El script de instalación de dependencias (install_dependencies) se encuentra ubicado en el folder denominado
   "Install_dependencies", para ejecutarlo sólo es necesario correr el siguiente comando:
   ./install_dependencies       

2- Una vez las condiciones y dependencias son cumplidas, el programa principal presenta un menú con
   diferentes opciones para escaneo y explotación de vulnerabilidades. 

Definición de subrutinas:
=========================

Golang:
=======

Se encuentran ubicadas en el folder "Modules" y clasificadas de la siguiente manera:

HYDRA_GO: Contiene el codigo encargado de ejecutar tyareas de pentesting mediante
          procedimiento de fuerza bruta.
          Los diccionarios para dicho procedimiento se encuentran ubicados en el
          folder denominado con el mismo nombre "Diccionarios".

NIKTO_GO: Contiene el código de ejecucion de la herramienta de escaneo de vulnerabilidades
          en aplicaciones/portales web, en esta utilidad es necesario especificar el puerto
          en el que se ejecuta la aplicación objetivo de la evaluación.

NMAP_GO: Contiene código de ejecución de varias operaciones con NMAP, tales como:
         - Revisión de CVE's
         - Revisión de vulnerabilidades
         - Revisión de puertos abiertos y disponibles. 

Bash:
=====
El programa principal se encuentra escrito en este intérprete.

Perl:
=====
La barra de progreso se encuentra escrita en perl, esta barra se encarga de monitorear
el progreso de ejecuciones de algunas tareas de instalación de dependencias.

Nmap:
=====
Herramienta con funcionalidades diversas enfocadas a la evaluación de vulnerabilidades.

Nikto:
======
Herramienta con funcionalidades diversas enfocadas a la evaluación de vulnerabilidades
en aplicaciones web.

Hydra:
======
Herramienta con funcionalidades de crackeo de credenciales enfocada a la penetración
de diversos sistemas informáticos y/o de comunicaciones mediante mecanismos de
fuerza bruta.


Desarrollado por:
 Francisco Javier Gutierrez G.
 Sr Linux Engineer
 fgutierrez@hexacta.com
 HEXACTA 2021

