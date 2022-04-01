def pds(ds):
    if len(ds) == 1:
        yield next(iter(ds))

    for d in ds:
        nds = frozenset(x for x in ds if x != d)
        for i in pds(nds):
            yield d + i


founds = []
for pd in pds(frozenset(str(x) for x in range(10))):
    found = True
    for i, p in enumerate((2, 3, 5, 7, 11, 13, 17)):
        if int("".join((pd[i + 1], pd[i + 2], pd[i + 3]))) % p > 0:
            found = False
            break

    if found:
        print("found", pd)
        founds.append(pd)

print(founds)
print(sum(int(f) for f in founds))
