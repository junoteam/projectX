#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: Kung Fury -*-

import socket
import urllib2
import os
import sys

class SystemUtils(object):

    VERSION_CENTOS_6_6 = 'Centos 6.6'
    VERSION_CENTOS_6_5 = 'Centos 6.5'
    VERSION_CENTOS_7 = 'Centos 7'

    # Check if Internet connection is working
    @staticmethod
    def check_internet_connection():
        try:
            url = 'http://www.google.com'
            data = urllib2.urlopen(url, timeout=1)
            print 'Connection to Internet is Ok \n'
        except urllib2.URLError as err:
            pass
            print 'You are not connected to Internet \n'

    # Check local hostname
    @staticmethod
    def check_host_name():
        host_name = socket.getfqdn()
        print "Hostname is: ", host_name

    # Check local IP address
    @staticmethod
    def check_local_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 0))
        local_ip_address = s.getsockname()[0]
        return local_ip_address

    # Check if user run CentOS 6.5 or 6.6
    @staticmethod
    def check_centos_version():
        if os.path.exists("/etc/redhat-release"):
            with open("/etc/redhat-release", 'r') as file:
                version = ''
                for line in file:
                    version += line
                if 'release 6.6' in version:
                    print 'You are using: ' + SystemUtils.VERSION_CENTOS_6_6
                elif 'release 6.5' in version:
                    print 'You are using: ' + SystemUtils.VERSION_CENTOS_6_5
                elif 'CentOS Linux release 7' in version:
                    print 'You are using: ' + SystemUtils.VERSION_CENTOS_7
                    file.close()
        else:
            print sys.version
            print 'Your version of Linux incompatible with this script, exit... \n'
            sys.exit()



