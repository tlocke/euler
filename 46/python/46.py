from itertools import count, dropwhile

primes = [2]

for i in count(3, step=2):
    print(i)
    maxp = int(i**0.5)
    if next(dropwhile(lambda x: i % x > 0 and x <= maxp, primes)) > maxp:
        primes.append(i)
    else:
        found = False
        for p in primes:
            for n in count(1):
                s = p + 2 * n**2
                if s > i:
                    break
                elif s == i:
                    found = True
                    break
        if not found:
            print("not found", i)
            break
