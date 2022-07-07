# Regular Expressions
# https://www.py4e.com/lessons/regex
"""
import re
fname = input("Enter ")
hand = open(fname)
for line in hand:
    line = line.rstrip()
    if re.search('^F..m:.+za', line):
        print(line)
"""
import re

hand = open("regex_sum_24962.txt")
x=list()
for line in hand:
     y = re.findall('[0-9]+',line)
     x = x+y

sum=0
for z in x:
    sum = sum + int(z)

print(sum)