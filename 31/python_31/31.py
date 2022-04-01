denoms = [200, 100, 50, 20, 10, 5, 2, 1]


def combos(dens, tot):
    if tot == 200:
        return 1

    if len(dens) == 0:
        return 0

    ndens = dens[1:]
    return sum(combos(ndens, i) for i in range(tot, 201, dens[0]))


print(combos(denoms, 0))
