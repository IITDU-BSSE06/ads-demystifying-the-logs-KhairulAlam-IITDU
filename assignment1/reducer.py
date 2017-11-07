#!/usr/bin/python

import sys

countIP = 0

for line in sys.stdin:
	
	thisIP = line.strip()
	
	if thisIP == "10.99.99.186":
		countIP += 1

print countIP
