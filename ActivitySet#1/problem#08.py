# Files 
\
#filename = "dataset/mbox-short.txt"
  # Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:    '): 
        continue
        numbers = line.split()
        store = line[:]
if inp.startswith('X-DSPAM-Confidence:    '):
    while True:
     total = 0
     colonpos = inp.find(':')
     host = inp[colonpos+4:]
     temp = float(host)
     total = total + temp
avg = total/count
print('Average spam confidence: %d',avg)                                                                                                                                              