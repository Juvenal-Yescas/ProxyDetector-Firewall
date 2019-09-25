import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',level=logging.DEBUG)

from proxydetectorfirewall.proxy_detector_firewall import ProxyDetectorFirewall
import pytest

proxy_detector_f = ProxyDetectorFirewall()
path= os.getcwd()

def compare_output(file_expected,file_output):
    with open(file_expected) as format_expected, open(file_output) as format_obteined:
        for l1, l2 in zip(format_expected, format_obteined):
            if l1 != l2:
                format_expected.close()
                format_obteined.close()
                return False
    format_expected.close()
    format_obteined.close()
    return True

def test_mikrotik():
    proxy_detector_f.detect_anonymous(path+'/tests/ExampleProxyList.txt','mikrotik',path+'/tests/mikrotik_output.txt')
    same_files=compare_output(path+'/tests/expectedfiles/mikrotik.txt',path+'/tests/mikrotik_output.txt')
    assert(same_files)

def test_iptables():
    proxy_detector_f.detect_anonymous(path+'/tests/ExampleProxyList.txt','iptables',path+'/tests/iptables_output.txt')
    same_files=compare_output(path+'/tests/expectedfiles/iptables.txt',path+'/tests/iptables_output.txt')
    assert(same_files)

def test_cisco_acl():
    proxy_detector_f.detect_anonymous(path+'/tests/ExampleProxyList.txt','cisco-acl',path+'/tests/cisco_acl_output.txt')
    same_files=compare_output(path+'/tests/expectedfiles/cisco_acl.txt',path+'/tests/cisco_acl_output.txt')
    assert(same_files)