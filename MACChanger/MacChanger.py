#!/usr/bin/env python3

import subprocess;
import optparse;

parser = optparse.OptionParser();

parser.add_option("-i","--interface",dest="interface",help="Interface to change MAC Address");
parser.add_option("-m","--mac",dest="new_mac",help="MAC Address to be changed");

options,arguments = parser.parse_args();

interface=options.interface
new_mac=options.new_mac

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
subprocess.call(["ifconfig",interface,"up"])

##ALTERNATE WAY FOR EXECUTING THE COMMANDS
# subprocess.call("ifconfig " + interface + " down",shell=True);
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac,shell=True);
# subprocess.call("ifconfig " + interface + " up",shell=True);

