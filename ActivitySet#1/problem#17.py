#lists
fname = input("Enter the file name:")
fh = open(fname)
count = 0
for line in fh:
    word = line.rstrip().split()
    if line.startswith ("From "):
        count += 1
        print(word[1])
    else:
        continue
print("There were",count,"lines in the file with From as the first word")