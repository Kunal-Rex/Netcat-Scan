#!/usr/bin/python3

import os
import sys

if(len(sys.argv) != 3):
	print('''[*]Enter <ip-range>/<prefix> <ports>(seperated by ",")		
[*]Example ./nc-scanner.py <ip-range> <ports>
		''')
else:
	ip_range = sys.argv[1]
	port = sys.argv[2].split(",")
	os.system("nmap -sn -n {} -oG - | awk '/Up$/{{print$2}}'>ip_list.txt".format(ip_range))


with open('ip-list.txt') as file:
	for i in file:
  		i = i.strip()
  		for j in range(len(port)):
  			cmd = f"nc -nv -w 1 -z {i} {port[j]}"
  			os.system(cmd)