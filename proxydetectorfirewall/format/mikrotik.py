#!/usr/bin/python3
# -*- coding: utf-8 -*-

try:
    from format.format import Format
except ImportError:
    from proxydetectorfirewall.format.format import Format


class Mikrotik(Format):

    def __init__(self):
        self.header_file = '\n/ip firewall address-list'

    def getFormat(self, ip):
        firewall_rule = 'add address={} comment="Proxy Anonymous" list=IP2Location'.format(
            ip
        )
        return firewall_rule
