<h1 align="center">
  ProxyDetector-Firewall
  
</h1>


  [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Juvenal-Yescas/ProxyDetector-Firewall/blob/master/LICENSE)
  [![Actions Status](https://github.com/Juvenal-Yescas/ProxyDetector-Firewall/workflows/Build/badge.svg)](https://github.com/Juvenal-Yescas/ProxyDetector-Firewall/actions)

## Description

**ProxyDetector-Firewall** is a script written in Python, enter an IP list and generate an output of the proxies detected with the rules for different firewalls to be applied directly.

The database used to recognize proxies can be obtained from [https://lite.ip2location.com/ip2proxy-lite](https://lite.ip2location.com/ip2proxy-lite) for free.

## Prerequisites

* Python3 
* pip3
* IP2Proxy - Proxy Detection Database

## Installation

```bash
pip3 install -r requirements.txt
```

Move your database `IP2PROXY-P[xxxx].BIN` to foder `/data/` as `IP2PROXY.BIN`
```
├── proxydetectorfirewall
│   ├── data
│   │   └── IP2PROXY.BIN
```
## Test

Tests on [Github Action](https://github.com/Juvenal-Yescas/ip2location-action/actions)

The `pytest` module is necessary

```
pip -q install pytest
```
##### Example:
```
pytest tests/output_files_test.py
```
## Usage

##### Examples: 
```
python3 cli.py -i listIps.txt -f cisco-acl
python3 cli.py -i listIps.txt -f cisco-acl -o rules-cisco.txt
```

#### Help how to use

```bash
python3 cli.py -h
```

```
usage: cli.py [-h] -i INPUT -f {iptables,mikrotik,cisco-acl} [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        File containing an ip list (default: None)
  -f {iptables,mikrotik,cisco-acl}, --firewall {iptables,mikrotik,cisco-acl}
                        Firewall, output format for the rules. (default: None)
  -o OUTPUT, --output OUTPUT
                        Output file with the rules to block the ips detected
                        as a proxy. (default: Output.txt)
```

## Build with

* [Python3](https://www.python.org/download/releases/3.0/) - Python is an interpreted, high-level, general-purpose programming language. 

### WIKI 

More information on how to use this project on the  [Wiki](https://github.com/Juvenal-Yescas/ip2location-action/wiki)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
