#!/usr/bin/env python3

import subprocess
import optparse
import re
from numpy.core import unicode

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="MAC Address to be changed")
    options,arguments = parser.parse_args()
    if not options.interface and not options.new_mac:
        parser.error("Please specify an interface and a new MAC Addsress, use --help for more info.")
    if not options.interface:
        parser.error("Please specify an interface, use --help for more info.")
    if not options.new_mac:
        parser.error("Please specify a new MAC Address, use --help for more info.")
    return options

def change_mac(interface,new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac_address(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    # unicode(ifconfig_result, encoding) used to convert bytes like object to string
    encoding = 'utf-8'
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", unicode(ifconfig_result, encoding))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("Could not read MAC Address.")

options= get_arguments()
interface=options.interface
new_mac=options.new_mac

current_mac_address=get_current_mac_address(interface)
print("MAC Address is " + str(current_mac_address))

change_mac(interface,new_mac)

current_mac_address=get_current_mac_address(interface)
if current_mac_address == new_mac:
    print("MAC Address was successfully changed to " + current_mac_address)
else:
    print("MAC Address was not changed.")
    
##ALTERNATE WAY FOR EXECUTING THE COMMANDS
# subprocess.call("ifconfig " + interface + " down",shell=True);
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac,shell=True);
# subprocess.call("ifconfig " + interface + " up",shell=True);

