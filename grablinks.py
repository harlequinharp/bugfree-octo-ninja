#!/usr/bin/env python
#a script that takes a file name (where file name is the argument to the grab links function) and prints all strings that follow href=
#written by Casey Merhige for Python 2.7
from __future__ import print_function
import re
from urllib import urlretrieve
from sys import argv

#first command line argument is file to search using reg ex
filename=argv[1]

#pattern to identify urls up to but not including closing double quote
pattern=r'(http://[^"]*)"'

#create empty list to save matched urls from loop below
files_to_down=[]

#loop through your text file to find matches to the reg ex above
with open(filename) as searchfile:
	for line in searchfile:
		match = re.search(pattern, line)
		if match:
			files_to_down.append(match.group(1))

#loop through urls, then, create new file named from end portion of url string. 
for url in files_to_down:
	stringparts=url.split("/")
	new_file_name=stringparts[-1]
	urlretrieve(url,new_file_name)