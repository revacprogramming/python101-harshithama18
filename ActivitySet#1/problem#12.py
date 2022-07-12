# Regular Expressions

import re

hand = input('enter')
fh = open(hand)
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x)




