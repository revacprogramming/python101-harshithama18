# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
       count = count + 1 
print('Line count',count) 
colonpos = fh.find('X-DSPAM-Confidence:')
host = fh[colonpos+1:]
avg = host/count
print('Average spam confidence: ')

