#!/usr/bin/python3

import os
import sys

if(len(sys.argv) != 3):
	print('''[*]Enter <ip-range>/<prefix> <ports>(seperated by ",")		
[*]Example ./nc_scan.py 192.168.10.128/24 53,80

		''')
	sys.exit(0)
else:
	ip_range = sys.argv[1]
	port = sys.argv[2].split(",")
	os.system("nmap -sn -n {} -oG - | awk '/Up$/{{print$2}}'>ip_list.txt".format(ip_range))
	with open('ip_list.txt') as file:
		for i in file:
	  		i = i.strip()
	  		for j in range(len(port)):
	  			cmd = f"nc -nv -w 1 -z {i} {port[j]}"
	  			os.system(cmd)
