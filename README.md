<p align="center">
  <a href="https://github.com/Juvenal-Yescas/ProxyDetector-Firewall/">
    <img src="https://www.iconfinder.com/icons/4417121/download/png/512" alt="ProxyDetector Firewall logo" width="119" height="119">
  </a>
</p>

<h3 align="center">ProxyDetector Firewall</h3>

<p align="center">
  Protect your infrastructure from incoming or outgoing Proxy connections. An extra layer of security to your network..
  <br>
  <a href="https://github.com/Juvenal-Yescas/ProxyDetector-Firewall/wiki/"><strong>Explore docs »</strong></a>
  <br>
  <br>
  <a href="https://github.com/Juvenal-Yescas/ProxyDetector-Firewall/issues">Report bug</a>
  ·
  <a href="https://github.com/Juvenal-Yescas/ProxyDetector-Firewall/issues">Request feature</a>
</p>

--- 
  [![Actions Status](https://github.com/Juvenal-Yescas/ProxyDetector-Firewall/workflows/Build/badge.svg)](https://github.com/Juvenal-Yescas/ProxyDetector-Firewall/actions)
  [![Python 3](https://img.shields.io/badge/python-3.0+-green.svg)](https://www.python.org/download/releases/3.0/)
  [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Juvenal-Yescas/ProxyDetector-Firewall/blob/master/LICENSE)

## Table of contents

- [Description](#description)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Run tests](#run-tests)
- [Usage](#usage)
- [Wiki](#wiki)
- [License](#license)

## Description 

**ProxyDetector-Firewall** is a script written in Python, enter an IP list and generate an output of the proxy detected with the rules for different firewalls to be applied directly.

Useful when it blocks the connection to improper sites and users bypass these rules using proxy.

The database used to recognize proxy can be obtained from :

 * [Free IP2Proxy BIN Data](https://lite.ip2location.com/ip2proxy-lite)
 * [Commercial IP2Proxy BIN Data](https://www.ip2location.com/database/ip2proxy)

##### Output formats supported:

* Mikrotik
* Cisco ACL
* Cisco bit bucket
* Linux iptables
* Juniper Junos
* CIDR

> Soon more will be added

## Prerequisites

* Python3 and up
* pip3
* IP2Proxy - Proxy Detection Database

## Installation

Clone the repository and enter its respective folder

```bash
pip3 install -r requirements.txt
```

Move your database `IP2PROXY-P[xxxx].BIN` to foder `/data/` as `IP2PROXY.BIN`
```
├── proxydetectorfirewall
│   ├── data
│   │   └── IP2PROXY.BIN
```

## Usage

```
usage: cli.py [-h] -i INPUT -f
              {iptables,mikrotik,cisco-acl,cidr,cisco-bitbucket,juniper-junos}
              [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        File containing an ip list (default: None)
  -f {iptables,mikrotik,cisco-acl,cidr,cisco-bitbucket,juniper-junos}, --firewall {iptables,mikrotik,cisco-acl,cidr,cisco-bitbucket,juniper-junos}
                        Firewall, output format for the rules. (default: None)
  -o OUTPUT, --output OUTPUT
                        Output file with the rules to block the ip detected
                        as a proxy. (default: Output.txt)
```

```
python3 cli.py -i ExampleProxyList.txt -f cisco-acl -o output.txt
python3 cli.py -i ExampleProxyList.txt -f mikrotik -o mikrotik.txt
```
###### Check out a demo

<a href="https://asciinema.org/a/qYuOoEJNzwsw1uRhf5g5hi4B6" target="_blank"><img src="https://asciinema.org/a/qYuOoEJNzwsw1uRhf5g5hi4B6.svg" /></a>

## Run tests

Tests on [Github Action](https://github.com/Juvenal-Yescas/ProxyDetector-Firewall/actions)

The `pytest` module is necessary

```
pip -q install pytest

pytest
pytest tests/output_files_test.py
```

## Build with

* [IP2Proxy](https://github.com/ip2location/ip2proxy-python) - IP2Proxy Python Library
* [Python3](https://www.python.org/download/releases/3.0/) - Python is an interpreted, high-level, general-purpose programming language. 

## Wiki

More information on how to use this project on the  [Wiki](https://github.com/Juvenal-Yescas/ProxyDetector-Firewall/wiki)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
