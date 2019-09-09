import sys

try:
    from proxy_detector_firewall import ProxyDetectorFirewall
except ImportError:
    from proxydetectorfirewall.proxy_detector_firewall import ProxyDetectionFirewall

if __name__ == '__main__':
    file_list_ip = str(sys.argv[1])
    format_firewall = str(sys.argv[2])
    file_output = str(sys.argv[3])
    af = ProxyDetectorFirewall()
    af.detect_anonymous(file_list_ip, format_firewall, file_output)
