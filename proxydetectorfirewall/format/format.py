#!/usr/bin/python3
# -*- coding: utf-8 -*-
# import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import sys
# import os.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)


class Format:

    def __init__(self):
        self.header_file = ''

    def get_header(self):
        return self.header_file

    def getFormat(self, ip):
        pass
