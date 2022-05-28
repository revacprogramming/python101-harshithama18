# Files

#filename = "dataset/mbox-short.txt"

  # Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
inp = fh.read()
if inp.startswith('X-DSPAM-Confidence:    '):
    count = 0
    for line in inp:
        count = count + 1  
if inp.startswith('X-DSPAM-Confidence:    '):
    sum = 0
    colonpos = inp.find(':')
    host = inp[colonpos+4:]
    for number in host:
        addi = float(add) + 1
card = float(addi)
avg = card/count
print('Average spam confidence: %d',avg)                                                                         