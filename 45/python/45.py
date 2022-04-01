from itertools import count


def tseqg():
    for n in count(1):
        yield n * (n + 1) // 2


def pseqg():
    for n in count(1):
        yield n * (3 * n - 1) // 2


def hseqg():
    for n in count(1):
        yield n * (2 * n - 1)


tseq = tseqg()
pseq = pseqg()
hseq = hseqg()

ts = set()
ps = set()
hs = set()

p = h = 0

while True:
    t = next(tseq)
    ts.add(t)

    if p < t:
        p = next(pseq)
        ps.add(p)

    if h < t:
        h = next(hseq)
        hs.add(h)

    found = ts & ps & hs
    if len(found) > 2:
        print("found", found)
        break
