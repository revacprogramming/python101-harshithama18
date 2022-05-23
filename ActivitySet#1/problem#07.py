# Strings

text = 'X-DSPAM-Confidence:    0.8475'
colonpos = text.find(':')
sppos = text.find('    ',colonpos)
host = text[colonpos+4:]
number = float(host)
print(number)
