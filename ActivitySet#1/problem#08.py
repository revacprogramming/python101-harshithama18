# Files 

#filename = "dataset/mbox-short.txt"
  # Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'): 
        continue
    t = line.find("0")
    number = float(line[t:])
    count += 1
    total = total + number
        #count =float(count)
avg = total/count
print(f'Average spam confidence: {avg}') 
guj