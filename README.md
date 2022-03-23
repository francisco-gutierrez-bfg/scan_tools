Security Scanning
=================
                                                         


Important:
==========

This tool has been developed to run exclusively on Ubuntu 18.x distributions and later.
It would possibly run on Debian, but has not been tested.  
A Python vulnerability scanner has also been added, which has the same functionality.

I'm still working on this but with limited time due to my current job.

Description:
============
System developed to evaluate and perform pentesting on computer systems in order to identify weak points,
This tool has not been developed for criminal purposes.
The use of the data and the effects that its execution may cause are the responsibility of the user and not the developer.
This tool has been developed for ethical purposes and strictly for the execution of laboratory activities.

Execution:
==========
./security   ---> In case you want to use the bash/golang script  
python security.py ---> In case you want to use the python script  
python3 security.py ---> In case you don´t have your environment set and you have python3 installed.

Execution reports:
======================
The execution of this utility makes a record of all its activity within the following path:
"Modules/REPORTES"


Components:
===========

This utility consists of several components, to achieve its operation you must take into account the following dependencies:
 - Golang (go1.13.8 linux/amd64)
 - Python 3.5.x
 - Perl 5.x
 - Nmap
   - Nmap Scripts Vulners
   - Nmap Scripts Vulscan
 - Hydra
 - Bash
 - Git

Main Program:
=============

The main program is written in bash, it contains some functions in perl and fulfills the following functions:

1- Verification of all the necessary dependencies for the correct functioning of the subroutines
   (Golang Scripts, NMAP Scripts).
   Without these dependencies the solution will not work, for this reason the main program will start the
   process of installation of dependencies automatically, requesting authorization and confirmation from the user.
   
   The installation of dependencies can be executed manually in the following way:  
   The dependencies installation script (install_dependencies) is located in the folder named "Install_dependencies", 
   to execute it it is only necessary to run the following command:  
   -  ./install_dependencies

2- Once the conditions and dependencies are fulfilled, the main program presents a menu with
   different options for scanning and exploitation of vulnerabilities.  

Sobroutines details:
====================

### Golang:


Each subroutine is located in a folder called "Modules" with the following structure:

HYDRA_GO:  Contains the code in charge of executing pentesting tasks through brute force procedure.     
           The dictionaries for this procedure are located in a folder called the same way "Dictionaries".  

NIKTO_GO:  Contains the execution code of the vulnerability scanning tool for web applications, it is necessary to specify the port    
           in which the target application of the evaluation is executed.  

NMAP_GO:   Contains execution code for multiple NMAP operations, such as:    
           - Review of CVEs  
           - Review of vulnerabilities   
           - Review of open and available ports     

Development details and tools used:  
===================================

### Bash:

The main program is written in this interpreter.  

### Perl:

The progress bar is written in perl, this bar is responsible for monitoring   
the execution progress of some dependency installation tasks.  

### Nmap:

Tool with diverse functionalities focused on the evaluation of vulnerabilities.  

### Nikto:

Tool with diverse functionalities focused on the evaluation of vulnerabilities
in web applications.

### Hydra:

Penetration-focused credential cracking tool of various computer and/or communication  
systems through mechanisms of brute force.


## Developed by:  
 Francisco Javier Gutierrez G.  
 Sr Linux Engineer  
 ingenierialinuxpereira@gmail.com  

