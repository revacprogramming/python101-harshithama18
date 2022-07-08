# Regular Expressions
# https://www.py4e.com/lessons/regex

import re
fname = input("Enter ")
hand = open(fname)
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:.+za', line):
        print(line)
