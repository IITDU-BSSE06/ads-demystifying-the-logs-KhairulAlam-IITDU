#!/usr/bin/python

import sys

count = 0
prevMethod = None

mapMethod = {}

for line in sys.stdin:
	token = line.strip()

	if token and token != prevMethod:
		count = 0

	prevMethod = token
	count += 1
	mapMethod[prevMethod] = count

for v in mapMethod:
	print "{0} {1}".format(v, mapMethod.get(v))
