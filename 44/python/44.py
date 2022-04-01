from collections import defaultdict
from itertools import count

pents = {1}
founds = defaultdict(set)

for n in count(2):
    p = n * (3 * n - 1) // 2

    for i in pents:
        diff = p - i
        if diff in pents:
            founds[p + i].add(diff)

    pents.add(p)

    if p in founds:
        print("found", sorted(founds[p])[0])
        break
