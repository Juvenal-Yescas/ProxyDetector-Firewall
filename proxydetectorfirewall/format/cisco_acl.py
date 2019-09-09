#!/usr/bin/python3
# -*- coding: utf-8 -*-
# import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import sys
# import os.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

try:
    from format.format import Format
except ImportError:
    from proxydetectorfirewall.format.format import Format


class CiscoACL(Format):

    def getFormat(self, ip):
        firewall_rule = 'deny ip {} any'.format(
            ip
        )
        return firewall_rule
