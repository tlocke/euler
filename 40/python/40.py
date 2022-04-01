from itertools import count
from math import prod


def chars():
    for p in count():
        for c in str(p):
            yield c


enum = enumerate(chars())
found = []
for sub in (10**i for i in range(7)):
    for x, c in enum:
        if x == sub:
            found.append(int(c))
            break


print(found)
print(prod(found))

"""
ds = []
place = -1
for p in range(7):
    place += 10**p * p
    ds.append(int(str(place + 1)[0]))

print(ds, prod(ds))
"""
