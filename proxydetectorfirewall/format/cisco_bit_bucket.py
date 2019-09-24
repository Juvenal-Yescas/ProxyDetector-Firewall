#!/usr/bin/python3
# -*- coding: utf-8 -*-

try:
    from format.format import Format
except ImportError:
    from proxydetectorfirewall.format.format import Format

class CiscoBitBucket(Format):

    def getFormat(self, ip):
        firewall_rule = 'ip route {}  255.255.255.255 Null0'.format(
            ip
        )
        return firewall_rule