#!/usr/bin/python

import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

f1 = open(str(file1), "r").readlines()
f2 = open(str(file1), "r").readlines()
#'''
#Can also use the code in quotes here:
set1 = set(f1)
set2 = set(f2)

print list(set1.difference(set2))

'''
def diff(list1, list2):
    c = set(list1).union(set(list2))
    d = set(list1).intersection(set(list2))
    return list(c - d)

diff = diff(f2, f1)
#print diff
for line in diff:
	print line
'''

# or do "sort file1 file2 | uniq -u"
