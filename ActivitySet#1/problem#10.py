# Dictionaries

#filename = "dataset/mbox-short.txt"
"""
txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))
t.sort(reverse=True)
res = list()
for length, word in t:
    res.append(word)
print(res)
"""
"""
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
"""
fname = input('Enter the file name:')
fh = open(fname)
counts = dict()
for line in fh:
    if line startswith ("From "):
        words = line.split()
        for word in words:
            if word[2] not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
lst = list()
for key,val in list(counts.tems()):
    lst.append((val,key))
lst.sort(reverse=True)
for key,val in lst

print()