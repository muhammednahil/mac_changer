#!/usr/bin/env python

import subprocess
import optparse
import re

def change_mac(interface , mac):
    print("[+] Changing MAC Address for " + interface)

    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)

def arg():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change MAC Address wlan0/eth0")
    parser.add_option("-m", "--new_mac", dest="mac", help="new MAC Address exaple 00:11:22:33:44:55")
    (options, argument) = parser.parse_args()
    if not options.interface:
        parser.error("[+] Please specify an interface, use --help for more info")
    elif not options.mac:
        parser.error("[+]Please specify an MAC Address, use --help for more info")
    return options

def cur_mac():
    current_mac = subprocess.check_output(["ifconfig", options.interface])
    re_cur_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", current_mac)
    if re_cur_mac:
        print("[+] Current MAC Address " + re_cur_mac.group(0))
    else:
        print("[+] Please specify an interface, use --help for more info")

def up_mac():
    updated_mac = subprocess.check_output(["ifconfig", options.interface])
    re_up_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", updated_mac)
    if re_up_mac:
        print("[+] Updated MAC Address " + re_up_mac.group(0))
    else:
        print("[-] Could not read MAC Address, use --help for more info.")

options =arg()
cur_mac()
change_mac(options.interface, options.mac)
up_mac()

