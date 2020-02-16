#!/usr/bin/env python3

import subprocess;

interface=input("Enter the interface");
new_mac=input("Enter the new MAC Address");

##ALTERNATE WAY
# subprocess.call("ifconfig " + interface + " down",shell=True);
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac,shell=True);
# subprocess.call("ifconfig " + interface + " up",shell=True);

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
subprocess.call(["ifconfig",interface,"up"])
