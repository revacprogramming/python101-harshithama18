# Files 
\
#filename = "dataset/mbox-short.txt"
  # Use the file name mbox-short.txt as the file name
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
inp = fh.read()
if inp.startswith('X-DSPAM-Confidence:    '):
    while True:
        count = 0
    for line in inp:
        count = count + 1  
if inp.startswith('X-DSPAM-Confidence:    '):
    while True:
    sum = 0
    colonpos = inp.find(':')
    host = inp[colonpos+4:]
    temp = float(host)
    sum = sum + temp
avg = sum/count
print('Average spam confidence: %d',avg)                                                                        