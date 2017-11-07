#!/usr/bin/python

import sys

for line in sys.stdin:
	row = line.strip().split(" ")
	if len(row) == 10:
		dirl = str(row[6])
		print dirl
