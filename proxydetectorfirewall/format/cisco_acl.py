#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
