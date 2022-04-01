from itertools import count, takewhile


def next_prime(primes):
    lp = len(primes)
    for i in count(primes[-1] + 1):
        if sum(1 for _ in takewhile(lambda x: i % x > 0, primes)) == lp:
            return i


def prime_factors(x):
    primes = [2]
    while primes[-1] < x:
        primes.append(next_prime(tuple(primes)))
    pfs = {}
    while x > 1:
        for p in primes:
            if x % p == 0:
                pfs[p] = pfs.get(p, 0) + 1
                x //= p
                break
    return pfs


def prod_pf(pf1, pf2):
    prod = pf1.copy()
    for k, v in pf2.items():
        prod[k] = prod.get(k, 0) + v
    return prod


def pf_to_num(pf):
    n = 1
    for k, v in pf.items():
        n *= k**v
    return n


def pf_normalize(pf):
    return {k: v for k, v in pf.items() if v != 0}


def pf_simplify(npf, dpf):
    for k in npf.keys() & dpf.keys():
        lowest = min(npf[k], dpf[k])
        npf[k] -= lowest
        dpf[k] -= lowest

    return pf_normalize(npf), pf_normalize(dpf)


def find():
    fracs = set()
    for denom in range(10, 100):
        denom_str = str(denom)
        denom_set = set(denom_str)
        denom_set.discard("0")
        for num in range(10, denom):
            num_str = str(num)
            for digit in set(num_str) & denom_set:
                nnum = int(num_str.replace(digit, "", 1))
                ndenom = int(denom_str.replace(digit, "", 1))
                if denom * nnum == ndenom * num:
                    fracs.add((num, denom))

    print(fracs)
    numpf = {}
    denompf = {}
    for n, d in fracs:
        npf = prime_factors(n)
        dpf = prime_factors(d)
        denompf = prod_pf(denompf, dpf)
        numpf = prod_pf(numpf, npf)
        print(n, npf, d, dpf)

    print(numpf, denompf)

    snumpf, sdenompf = pf_simplify(numpf, denompf)
    print(snumpf, sdenompf)

    print(pf_to_num(snumpf), pf_to_num(sdenompf))


find()
