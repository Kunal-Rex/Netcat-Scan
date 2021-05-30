#!/bin/sh
nmap 192.168.10.129/24 -sn -n -oG -| awk '/Up$/{print $2}'>ip-list.txt
while read l;do nc -nv -w 1 -z $l 53;done < ip-list.txt