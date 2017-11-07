#!/usr/bin/python

import sys

countFD = 0

for line in sys.stdin:
	FD = line.strip()
	
	if FD == "/assets/js/the-associates.js":
		countFD += 1

print countFD
