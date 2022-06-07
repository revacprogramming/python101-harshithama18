# Files 

#filename = "dataset/mbox-short.txt"
  # Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith('X-DSPAM-Confidence: '): 
        continue
  t = find.line(" ")
  
  count+ = 1
  total+ = number  
avg = total/count
print('Average spam confidence: %d',avg)