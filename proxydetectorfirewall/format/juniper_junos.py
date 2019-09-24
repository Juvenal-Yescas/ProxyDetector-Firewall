#!/usr/bin/python3
# -*- coding: utf-8 -*-

try:
    from format.format import Format
except ImportError:
    from proxydetectorfirewall.format.format import Format

class JuniperJunos(Format):

    def getFormat(self, ip):
        firewall_rule = 'set {}/32'.format(
            ip
        )
        return firewall_rule