from itertools import count, filterfalse, dropwhile


def pwrs(p):
    m = 9**p
    b = next(dropwhile(lambda x: 10**x < x * m, count(2))) * m + 1
    return sum(x for x in range(2, b) if sum(int(c) ** p for c in str(x)) == x)


print(pwrs(4))
print(pwrs(5))
