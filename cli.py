#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

from proxydetectorfirewall.proxy_detector_firewall import ProxyDetectorFirewall

if __name__ == '__main__':
    file_list_ip = str(sys.argv[1])
    format_firewall = str(sys.argv[2])
    file_output = str(sys.argv[3])
    af = ProxyDetectorFirewall()
    af.detect_anonymous(file_list_ip, format_firewall, file_output)