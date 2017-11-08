#!/usr/bin/python

import sys

count = 0
maxCount = 0
prevYear = None
year = None

mapYear = {}

for line in sys.stdin:
	token = line.strip()

	if token and token != prevYear:
		if count >= maxCount:
			maxCount = count
			year = prevYear
		count = 0
		prevYear = token

	prevYear = token
	count += 1
	mapYear[prevYear] = count
	
if count >= maxCount:
	maxCount = count
	year = prevYear

for v in mapYear:
	print "{0} {1}".format(v, mapYear.get(v))

print "Year ", year, " had most number of hits" 
