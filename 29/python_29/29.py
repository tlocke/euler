from itertools import dropwhile


def num_distinct(size):
    pfs = {}
    primes = []
    distinct = set()

    for a in range(2, size + 1):
        try:
            p = next(dropwhile(lambda x: a % x > 0, primes))
            pf = pfs[a // p].copy()
            pf[p] = pf.get(p, 0) + 1
        except StopIteration:
            primes.append(a)
            pf = {a: 1}

        for b in range(2, size + 1):
            distinct.add(tuple([(k, v*b) for k, v in sorted(pf.items())]))

        pfs[a] = pf

    return len(distinct)


def run(size):
    print(f"size {size} num_distinct {num_distinct(size)}")


run(5)
run(100)
