import re
hand = open('sample1.txt')
numlist = []
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    if len(stuff) <= 0:
        continue
    for i in stuff:
        numlist.append(int(i))
print('Sum: ', sum(numlist))
