#!/usr/bin/python3
# -*- coding: utf-8 -*-

try:
    from format.format import Format
except ImportError:
    from proxydetectorfirewall.format.format import Format


class IpTables(Format):

    def getFormat(self, ip):
        firewall_rule = 'iptables -A INPUT -s {} -j DROP'.format(
            ip
        )
        return firewall_rule
