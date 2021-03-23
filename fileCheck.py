import re
fhand = open('output.txt')
numlist = list()
for line in fhand:
    line = line.rstrip()
    y = re.findall('[0-9]+', line)
    if len(y) <= 0:
        continue
    num = float(y[0])
    numlist.append(num)

print(max(numlist))
