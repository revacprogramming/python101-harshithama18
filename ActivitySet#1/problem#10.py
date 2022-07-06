# Dictionaries

#filename = "dataset/mbox-short.txt"
fname = input("Enter the name of the file: ")
fh = open(fname)
lst = list()
for line in fh:
    if line.startswith("From "):
        line = line.split()
        lst.append(line[1])
counts = dict()
for word in lst:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1
maxcount = None
maxcount = None
for word,count in counts.items():
    if maxcount is None or count > maxcount:
        maxcount = count
        maxword = word
print(maxword,maxcount)