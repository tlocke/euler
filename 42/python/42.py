from collections import defaultdict
from itertools import count


comp = defaultdict(int)
with open("../words.txt") as f:
    for line in f.readlines():
        for raw_word in line.split(","):
            w = raw_word[1:-1]
            comp[sum((ord(c) - 64) for c in w)] += 1


def trigs(m):
    for n in count(1):
        t = n * (n + 1) / 2
        yield t
        if t > m:
            break


r = sum(comp.get(t, 0) for t in trigs(max(comp.keys())))

print(r)
