#!/usr/bin/python

import sys

count = 0
maxCount = 0
previousFile = None
filename = None

for line in sys.stdin:
	token = line.strip()

	if token and token != previousFile:
		if count >= maxCount:
			maxCount = count
			filename = previousFile		
		count = 0
		previousFile = token
	
	previousFile = token
	count += 1

if count >= maxCount:
	maxCount = count
	filename = previousFile

print filename
