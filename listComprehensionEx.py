from datetime import datetime
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_len = []
for word in words:
    if word != "the":
        word_len.append(len(word))
print(words)
print(word_len)

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_len = [len(word) for word in words if word != "the"]
print(words)
print(word_len)

nums = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
print([int(num) for num in nums if num > 0])

myString = 'hello'
myFloat = 10.0
myInt = 20

if myString == 'hello':
    print('String: %s' % myString)
if isinstance(myFloat, float) and myFloat == 10.0:
    print('Float: %f' % myFloat)
if isinstance(myInt, int) and myInt == 20:
    print("Integer: %d" % myInt)

for n in range(1, 11):
    sentence = f'The value is {n:02}'
    print(sentence)

birthday = datetime(1990, 1, 1)
sentence = f'Jenn has a birthday on {birthday: %B %d, %Y}'
print(sentence)

myList = [1, 2, 3]
print([1, 2, 3])


numbers = []
strings = []
name = ['John', 'Eric', 'Jessica']
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append('hello')
strings.append('world')
secondName = name[1]
print(numbers)
print(strings)
print('The second name on the names list is %s' % secondName)

x = object()
y = object()

xList = [x]*10
yList = [y]*10
bigList = xList+yList

print('xList contains %d objects' % len(xList))
print('yList contains %d objects' % len(yList))
print('bigList contains %d objects' % len(bigList))

if xList.count(x) == 10 and yList.count(y) == 10:
    print('Almost there...')

if bigList.count(x) == 10 and bigList.count(y) == 10:
    print('Great!')

data = ('John', 'Doe', 53.44)
formatString = 'Hello %s %s. Your current balance is $ %s'

print(formatString % data)

aStr = "Hello World!"
afewWords = aStr.split(" ")
print(afewWords)

aStr = 'Hello World!'
print(aStr[::-5])

s = 'Hey there! what should this string be?'
print(len(s))
print("length of s" % len(s))
print('The first occurance of the letter a = %d' % s.index("a"))
print('a occurs %d times' % s.count("a"))
print('The first five characters are '$s'" % s[:5])
print("The next five characters are '%s" % s[5:10])
print("The thirteenth character is'" % s[12])
print(The characters with odd index are '%s'" % s[1::2])
print("The last five characters are '%s'" % s[-5:])
print('String in uppercase: %s' % s.upper(s))
print('String in lowercase: %s' % s.lower(s))
if s.startswith("Str"):
    print("String starts with 'str'. Good!")
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")
print('Split the words of the string: %s' s.split(" "))
