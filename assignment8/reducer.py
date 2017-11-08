#!/usr/bin/python

import sys

count = 0
prevFile = None

mapFile = {}

for line in sys.stdin:
	token = line.strip()

	if token and token != prevFile:
		count = 0

	prevFile = token
	count += 1
	mapFile[prevFile] = count

for v in mapFile:
	print "{0} {1}".format(v, mapFile.get(v))
