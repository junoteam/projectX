## LAMP Deploy Script for CentOS 6.5/6.6 systems
Very first and 'raw' version of LAMP Deploy Script. LAMP Deploy Script - written with Python 2.7 and should run "out of the box" on CentOS 6.5/6.6 systems. Script was written to help web developers and any new user in Linux to deploy his own, ready to use web server. In one click user can install Apache, MySQL and PHP.

## What script do?
- Add EPEL & IUS repository to the system
- Install latest and stable Apache web server
- Install MySQL Community Server Repository
- Install latest and stable MySQL Community Server
- Install all necessary PHP packages

Script also has support of "Additional tools" that do:
- Check version of your system
- Check if you are connected to the Internet
- Check your local IP address

## To do list:
- To add full support of Centos 7 (both LEMP & LAMP stacks)
- To add LEMP stack (Linux, NGinx, MySQL, PHP-FPM with FastCGI)
- To add option `1-click install LAMP stack`
- To add option `1-click install LEMP stack`
- To add option `Additional tools`
- Different versions of PHP 5.4, 5.5 or 5.6
- Support of SSL
- CSF - ConfigServer Security & Firewall (optional)
- Support of `PhpMyAdmin`
- Create one binary file by using Cython library (optional)
- To add full support of Ubuntu 12.04/14.04 LTS (optional)
- Fixing bugZZzzz

## How-to use
For now, script contains only two files written on Python:
* RunStaFF.py
* Centos66_64bit_LAMP.py

You should run `Centos66_64bit_LAMP.py` to see "Welcome Screen"
LAMP Deploy Script has been checked only on 64-bit CentOS, you should avoid to use on 32-bit server.
Script will not run, if you don't use CentOS 6.5/6.6

## Warning, BUGZZzz
This script still contains bugs and it need a lot of polish.
