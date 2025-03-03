import random

a = random.randint(1, 9)
b = random.choice('abcdefghijkilmnopqrstuvwxyz')
c = random.choice('ABCDEFGHIJKILMNOPQRSTUVWXYZ')
d = random.choice('!@#$%^&*()')
e = str(a) + str(b) + str(c) + str(d)+str(a) + str(b) + str(c) + str(d)

print(f"random generated number {e}")