#!/usr/bin/python

import sys

counter = 0
previousFile = None

for line in sys.stdin:
	filename = line.strip()

	if filename != previousFile:
		previousFile = filename
		counter += 1

print counter 
