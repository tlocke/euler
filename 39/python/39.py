def irt(max_p):
    found = {}
    for a in range(1, max_p - 2):
        for b in range(a, max_p - a - 2):
            for c in range(b + 1, max_p - a - b - 2):
                if a**2 + b**2 == c**2:
                    p = a + b + c
                    try:
                        founds = found[p]
                    except KeyError:
                        founds = found[p] = []

                    comb = a, b, c
                    founds.append(comb)
                    print("found comb", comb, "p", p)

    print(found[120])
    sol = None
    maxlen = 0
    for k, v in found.items():
        if len(v) > maxlen:
            sol = k, v
            maxlen = len(v)

    print(sol)


irt(1000)
"""
def irt(p):
    for comb in combinations_with_replacement(list(range(1, p)), 3):
        if comb[0] ** 2 + comb[1] ** 2 == comb[2] ** 2:
            p = comb[0] + comb[1] + comb[2]
            try:
                founds = found[p]
            except KeyError:
                founds = found[p] = []

            founds.append(comb)
            print("found comb", comb, "p", p)

    print(found[120])
    sol = None
    maxlen = 0
    for k, v in found.items():
        if len(v) > maxlen:
            sol = k, v
            maxlen = len(v)

    print(sol)


"""
