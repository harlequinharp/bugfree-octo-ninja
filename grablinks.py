#!/usr/bin/env python
# a script that takes a file name (where file name is the argument to the grab links function) and prints all strings that follow href=
import re
from sys import argv
filename=argv[1]

print(argv[1])

pattern=r'href ?= ?"(.*)"'

with open(filename) as searchfile:
	for line in searchfile:
		match = re.search(pattern, line)
		if match:
			print(match.group(1))
		else:
			print('Nope, I''ll try again...')
