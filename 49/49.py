from itertools import (
    combinations,
    combinations_with_replacement,
    dropwhile,
    permutations,
)

primes = [2]

for i in range(3, 10000, 2):
    maxp = int(i**0.5)
    if next(dropwhile(lambda p: i % p > 0 and p <= maxp, primes)) > maxp:
        primes.append(i)

found = []

for comb in combinations_with_replacement("".join(str(i) for i in range(10)), 4):
    perms = set(int("".join(p)) for p in permutations(comb, 4) if p[0] != "0")
    perms = [p for p in perms if p in primes]
    for c in combinations(perms, 3):
        if c[2] - c[1] == c[1] - c[0]:
            found.append(c)

print("end found", found, "".join(str(f) for f in found[-1]))
