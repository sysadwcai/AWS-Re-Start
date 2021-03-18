msg = 'It was a bright cold day in April, and the clocks were striking thirteen. '

count = 0

for character in msg.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
