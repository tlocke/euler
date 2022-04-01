from itertools import count, dropwhile
from math import factorial as fac

m = next(dropwhile(lambda x: 10**x < x * fac(9), count(1))) * fac(9)
s = sum(i for i in range(3, m) if sum(fac(int(d)) for d in str(i)) == i)
print(s)
