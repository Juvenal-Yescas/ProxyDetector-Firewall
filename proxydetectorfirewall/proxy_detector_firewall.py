#!/usr/bin/python3
# -*- coding: utf-8 -*-

import IP2Proxy
import os
import logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

try:
    from format.mikrotik import Mikrotik
    from format.iptables import IpTables
    from format.cisco_acl import CiscoACL
except ImportError:
    from proxydetectorfirewall.format.mikrotik import Mikrotik
    from proxydetectorfirewall.format.iptables import IpTables
    from proxydetectorfirewall.format.cisco_acl import CiscoACL

class ProxyDetectorFirewall:

    def __init__(self):
        self.__db = IP2Proxy.IP2Proxy()
        path = os.getcwd()
        self.__db.open(
            path+"/proxydetectorfirewall/data/IP2PROXY-LITE-PX1.BIN")

    def detect_anonymous(self, file_list_ip, format_firewall, name_file_output):
        self.__firewall = self.__get_firewall(format_firewall)

        try:
            self.__firewall.get_header()
        except AttributeError:
            print("Oops! The firewall format is not valid.")
            exit(1)

        logging.debug(self.__firewall)

        file_output = open(name_file_output, "w+")
        file_output.write('%s\r\n' % '# -------------------------------------------------------'
                                     + '# Free IP2Proxy Firewall List\n'
                                     + '# https://lite.ip2location.com/ip2proxy-lite\n'
                                     + '# [Important] Please update this list every month\n'
                                     + '# -------------------------------------------------------')
        # Write header some firewalls
        file_output.write('%s\r\n' % self.__firewall.get_header())
        try:
            list_ip = open(file_list_ip, 'r', encoding='utf-8-sig')
        
        except FileNotFoundError:
            print("Could not open input file.")
            exit(1)

        while True:
            ip = list_ip.readline()  # Get next line from file
            ip = ip.replace('\n', '')

            if not ip:  # If line is empty then end of file reached
                break

            if self.__db.is_proxy(ip) == 1:
                logging.debug('%s -> is an anonymous Proxy', ip)
                file_output.write('%s\r\n' % self.__firewall.getFormat(ip))
            else:
                logging.debug('%s is not a Proxy', ip)
        list_ip.close()
        file_output.close()
        self.__db.close()

    def __get_firewall(self, format_firewall):
        list_formats = {
            'mikrotik': Mikrotik(),
            'iptables': IpTables(),
            'ciscoacl': CiscoACL()
        }
        return list_formats.get(format_firewall, None)