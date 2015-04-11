#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: Alex Berber-*-

from Centos6Bit64 import *

# Checking version of OS should happened before menu appears
# Check version of CentOS
Centos6.check_centos_version()

# Clear screen before to show menu
os.system('clear')

answer = True
while answer:
    print ("""
    LAMP Deploy Script V: 0.1 for CentOS 6.5/6.6 64Bit:
    ---------------------------------------------------

    1. Check version of your CentOS
    2. Check Internet connection
    3. Show me my local IP address
    4. Open port 80 to Web

    ------- LAMP for CentOS 6 -----------
    5. Install EPEL & IUS repository
    6. Install Web Server - Apache
    7. Install Database - MySQL
    8. Install Language - PHP
    9. Help with LAMP in CentOS
    10. Exit/Quit
    """)

    answer = input("Please make your choice: ")
    if answer == 1:
        print ('\nChecking version of the system: ')
        Centos6.check_centos_version()
    elif answer == 2:
        print ('\nChecking if you connected to the Internet')
        Centos6.check_internet_connection()
    elif answer == 3:
        print ('\nYour local IP address is: ' + Centos6.check_local_ip())
    elif answer == 4:
        print('\nChecking firewall')
        Centos6.iptables_port()
    elif answer == 5:
        print ('\nInstalling EPEL and IUS repository to the system...')
        Centos6.add_repository()
    elif answer == 6:
        print ('\nInstalling Web Server Apache...')
        Centos6.install_apache()
    elif answer == 7:
        print ('\nInstalling database MySQL...')
        Centos6.install_mysql()
    elif answer == 8:
        print('\nInstalling PHP...')
        Centos6.install_php()
    elif answer == 9:
        print ('Help')
    elif answer == 10:
        print("\nGoodbye...\n")
        answer = None
    else:
        print ('\nNot valid Choice, Try Again')
        answer = True