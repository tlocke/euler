from itertools import dropwhile
from math import ceil


def pandigitals(ds):
    if len(ds) == 1:
        yield next(iter(ds))
    else:
        for d in ds:
            dsc = ds.copy()
            dsc.remove(d)
            for p in pandigitals(dsc):
                yield d + p


def pd(maxd):
    primes = [2]
    for n in range(2, int(10 ** ceil(maxd / 2))):
        maxp = int(n**0.5)

        if next(dropwhile(lambda x: n % x != 0 and x <= maxp, primes)) > maxp:
            primes.append(n)
    print("found primes")

    for md in range(maxd, 0, -1):
        founds = []
        pset = {str(i) for i in range(1, md + 1)}
        print("doing pset", pset)
        for pd in map(int, pandigitals(pset)):
            # print(pd)
            maxp = int(pd**0.5)
            ir = dropwhile(lambda x: pd % x != 0 and x <= maxp, primes)
            if next(ir) > maxp:
                print("found", pd)
                founds.append(pd)
        if len(founds) > 0:
            break

    print(founds)
    print(sorted(founds)[-1])


pset = {str(i) for i in range(1, 4 + 1)}
print(list(pandigitals(pset)))
pd(9)
