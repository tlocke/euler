from itertools import combinations, dropwhile, permutations

primes = [2]

for i in range(3, 10000, 2):
    maxp = int(i**0.5)
    if next(dropwhile(lambda p: i % p > 0 and p <= maxp, primes)) > maxp:
        primes.append(i)

found = []

for comb in combinations("".join(str(i) for i in range(10)), 4):
    print(comb)
    perms = [int("".join(p)) for p in permutations(comb, 4)]
    print("perms", perms)
    perms = [p for p in perms if p in primes]
    print("prime perms", perms)
    for c in combinations(perms, 3):
        # print("c", c)
        if c[2] - c[1] == c[1] - c[0]:
            found.append(c)

    """
    if len(found) > 1:
        # print("found", found)
        break
    """

    """
    if "0" in comb and "9" in comb:
        break
    """

    """
    if 1487 in perms:
        print("1487", perms, "found", found)
        break
    """

print("end found", found)
