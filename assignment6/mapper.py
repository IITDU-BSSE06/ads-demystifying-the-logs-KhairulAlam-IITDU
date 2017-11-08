#!/usr/bin/python

import sys

for line in sys.stdin:
	row = line.strip().split(" ")

	if len(row) == 10:
		hit = str(row[3])
		t1 = hit.strip().split(":")
		t2 = str(t1[0])
		t3 = t2.strip().split("/")
		t4 = str(t3[2])
		print t4
