from itertools import count, dropwhile

primes = [2, 3, 5, 7]
found = []
for i in count(8):
    max_p = int(i**0.5)

    if next(dropwhile(lambda x: i % x > 0 and x <= max_p, primes)) > max_p:
        primes.append(i)

        istr = str(i)
        passed = True
        for j in range(1, len(istr)):
            if int(istr[j:]) not in primes:
                passed = False
                break
            if int(istr[:-j]) not in primes:
                passed = False
                break

        if passed:
            found.append(i)
            print("found", i)
            if len(found) == 11:
                break


print(found, sum(found))
