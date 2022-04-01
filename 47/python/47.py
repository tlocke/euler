from itertools import count


def find(d):
    primes = [2]
    cons = []
    for i in count(2):
        factors = set()
        c = i
        while c > 1:
            for p in primes:
                n, r = divmod(c, p)
                if r == 0:
                    factors.add(p)
                    c = n
                    break

            if c == i:
                primes.append(i)
                break

        if len(factors) == d:
            cons.append(i)
            if len(cons) == d:
                print("found", cons[0])
                break
        else:
            cons.clear()


find(2)
find(3)
find(4)
