#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: AlexB -*-

import os
import subprocess

class Centos6Deploy(object):

    # Open port 80 in IPtables firewall
    @staticmethod
    def iptables_port():
        if os.path.exists('/etc/sysconfig/iptables'):
            with open('/etc/sysconfig/iptables', 'r') as file:
                checkport = ''
                for line in file:
                    checkport += line
                if '--dport 80' in checkport:
                    print 'Port 80 is open'
                    file.close()
                else:
                    file = open('/etc/sysconfig/iptables', 'r')
                    contents = file.readlines()
                    file.close()

                    file = open("/etc/sysconfig/iptables", "w")
                    contents.insert(6, '-A INPUT -p tcp -m tcp --dport 80 -j ACCEPT\n')
                    contents = "".join(contents)
                    file.write(contents)
                    file.close()
                    os.system('/etc/init.d/iptables restart' + ' > /dev/null 2>&1')

                    print 'Port 80 is closed'
                    print 'Openning ... '

    # Add EPEL and REMI repository to the system
    @staticmethod
    def add_repository():
        ### Check for EPEL repository
        if os.path.exists('/etc/yum.repos.d/epel.repo'):
            print 'Repository EPEL exist...'
        ### Check for IUS repository
        elif os.path.exists('/etc/yum.repos.d/ius.repo'):
            print 'Repository IUS exist...'
        else:
            # Installing EPEL & IUS repository
            if os.path.exists('/tmp/projectx/repos'):
                print 'Installing repository EPEL & IUS'
                os.system('sudo yum install wget' + " > /dev/null 2>&1")
                os.chdir('/tmp/projectx/repos')
                os.system('wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm')
                os.system('wget http://dl.iuscommunity.org/pub/ius/stable/CentOS/6/x86_64/ius-release-1.0-13.ius.centos6.noarch.rpm')
                os.system('sudo rpm -Uvh /tmp/projectx/repos/ius-release*.rpm')
                os.system('sudo rpm -Uvh /tmp/projectx/repos/epel-release-6*.rpm')

            else:
                os.makedirs('/tmp/projectx/repos')
                os.chdir('/tmp/projectx/repos')
                os.system('yum install wget -y' + " > /dev/null 2>&1")
                print 'Installing repository EPEL & IUS'
                os.system('wget http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm')
                os.system('wget http://dl.iuscommunity.org/pub/ius/stable/CentOS/6/x86_64/ius-release-1.0-13.ius.centos6.noarch.rpm')
                os.system('sudo rpm -Uvh /tmp/projectx/repos/epel-release-6*.rpm')
                os.system('sudo rpm -Uvh /tmp/projectx/repos/ius-release*.rpm')

    # Install web server Apache in CentOS 6.5, 6.6
    @staticmethod
    def install_apache():
        proc = subprocess.Popen(['rpm -qa | grep httpd'], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        if 'httpd-2.2' in out:
            print 'WARNING!: Apache is already installed in the System... Stop'
            #sys.exit()
        else:
            os.system('sudo yum install httpd -y')
            os.system('sudo service httpd start')
            os.system('sudo chkconfig --level 235 httpd on')
            #os.system('clear')
            print 'Apache successfully installed into the system'
            print 'Go to your local IP ' + Centos6Deploy.check_local_ip() + ' in browser to check it '

    # Install MySQL DB in CentOS 6.5, 6.6
    @staticmethod
    def install_mysql():
        proc = subprocess.Popen(['rpm -qa | grep mysql'], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        if 'mysql-community-server' in out:
            print 'WARNING!: MySQL Community server is already installed in the system'
        else:
            if not os.path.exists('/tmp/projectx/mysql'):
                os.makedirs('/tmp/projectx/mysql')
                os.chdir('/tmp/projectx/mysql')

                # This install Repository
                os.system('wget http://repo.mysql.com/mysql-community-release-el6-5.noarch.rpm' + " > /dev/null 2>&1")
                os.system('sudo rpm -Uvh mysql-community-release-el6-5.noarch.rpm')

                # This install DB MySQL Community Edition
                os.system('sudo yum install mysql-community-server -y')
                os.system('/etc/init.d/mysqld start')
                os.system('chkconfig --level 235 mysqld on')
            else:
                os.chdir('/tmp/projectx/mysql')
                if os.path.isfile('http://repo.mysql.com/mysql-community-release-el6-5.noarch.rpm'):
                    os.system('sudo rpm -Uvh mysql-community-release-el6-5.noarch.rpm')
                else:
                    os.system('wget http://repo.mysql.com/mysql-community-release-el6-5.noarch.rpm' + " > /dev/null 2>&1")
                    os.system('sudo rpm -Uvh mysql-community-release-el6-5.noarch.rpm')
                    os.system('sudo yum install mysql-community-server -y')
                    os.system('/etc/init.d/mysqld start')
                    os.system('chkconfig --level 235 mysqld on')

    # Install server-side scripting language PHP
    @staticmethod
    def install_php():
        os.system('yum install php php-mysql php-mbstring php-pear php-common php-devel php-cli -y')
        os.system('/etc/init.d/httpd restart')
        os.system('/etc/init.d/mysqld restart')
        print ('PHP is installed successfully')