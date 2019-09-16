import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',level=logging.DEBUG)

from proxydetectorfirewall.proxy_detector_firewall import ProxyDetectorFirewall
import pytest

proxy_detector_f = ProxyDetectorFirewall()
path= os.getcwd()

def test_format_not_valid():
    with pytest.raises(SystemExit):  
        assert proxy_detector_f.detect_anonymous(path+'/tests/ExampleProxyList.txt','nothing',path+'/tests/cisco_acl_output.txt')

def test_input_file_doesnt_exist():
    with pytest.raises(SystemExit):  
        assert proxy_detector_f.detect_anonymous(path+'/tests/nofile.txt','mikrotik',path+'/tests/cisco_acl_output.txt')