# Tuples

#filename = "dataset/mbox-short.txt"
"""
def print_twice(bruce):
    print(bruce)
    print(bruce)
"""
fname = input("Enter the name of the file: ")
fh = open(fname)
d = dict()
for line in fh:
    if line.startswith("From "):
        line = line.split()
        line = line[5]
        line = line[0:2]
        d[line] = d.get(line,0)+1
lst = list()
for value,count in d.items():
    lst.append((value,count))
lst.sort()
for value,count in lst:
    print(value,count)