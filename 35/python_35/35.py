from itertools import takewhile

primes = ["2"]
ps = [2]

imax = 1000000
ps_max = int(imax**0.5)
for i in range(2, imax):
    if sum(1 for p in takewhile(lambda x: i % x > 0, ps)) == len(ps):
        primes.append(str(i))
        if i <= ps_max:
            ps.append(i)
        print(i)

print(primes)

rp = set()
for p in primes:
    if p in rp:
        continue
    isrp = True
    for i in range(1, len(p)):
        if p[i:] + p[:i] not in primes:
            isrp = False
            break
    if isrp:
        print("adding", p)
        rp.add(p)

print(rp)
print("size rp", len(rp))
