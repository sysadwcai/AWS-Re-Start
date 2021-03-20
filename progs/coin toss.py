# coin toss
import random
import time
heads = 0

for i in range(1, 101):
    if random.randint(0, 1) == 1:
        heads += 1
    if i == 50:
        print('halfway done!')
        time.sleep(3)
print('heads came up ' + str(heads) + ' times.')
