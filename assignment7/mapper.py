#!/usr/bin/python

import sys

for line in sys.stdin:
	row = line.strip().split(" ")

	if len(row) == 10:
		method = str(row[5])
		t1 = method.strip().split('"')
		t2 = str(t1[1])
		print t2
