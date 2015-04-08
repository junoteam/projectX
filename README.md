## LAMP Deploy Script for Centos 6.5/6.6 systems
Very first and 'raw' version of LAMP Deploy Script. LAMP Deploy Script - written with Python 2.7 and should run "out of the box" on Centos 6.5/6.6 systems. 


## LAMP Deploy Script V 0.1
LAMP Deploy Script was written to help web developers and any new user in Linux to deploy his own, ready to use web server. In one click user can install Apache, MySQL and PHP. 


## To Do list:
- To add full support of Centos 7 
- To add full support of Ubuntu 12.04/14.04 LTS
- To add LEMP stack (Linux, NGinx, MySQL, PHP)
- To add option '1-click install'
- To add option 'Additional tools'
- Create one binary file by using Cython library

## Warning, BUGZZzz
This script still conteins bugs and it need a lot of polish. 

## How-to use
For now, script contains only two files written on Python:
- Centos66_64bit_LAMP.py
- RunStaFF.py
If you want to try it out, just run Centos66_64bit_LAMP.py like this:


	# python Centos66_64bit_LAMP.py

    LAMP Deploy Script V: 0.1:
    --------------------------

    1. Check version of your Centos/RHEL
    2. Check Internet connection
    3. Show me my local IP address
    ------- LAMP for CentOS 6 -----------
    4. Install EPEL & IUS repository
    5. Install Web Server - Apache
    6. Install Database - MySQL
    7. Install PHP
    8. Help with LAMP in CentOS
    9. Exit/Quit

	Please make your choice:

Script contains logic for using sudo, but it's better run its with root privileges because it would install all necessary repositories and packages. **Run this script only on 'clean' and 'fresh-intalled' system.** 







