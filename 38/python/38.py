from itertools import count


def pandig(max_i):
    found = []
    full = [str(i) for i in range(1, 10)]
    print("full", full)

    for i in range(1, max_i):
        for n in count(2):
            pstr = "".join(str(j * i) for j in range(1, n + 1))
            # print("i", i, "n", n, "pstr", pstr)
            lpstr = len(pstr)
            if lpstr > 9:
                break
            elif lpstr == 9 and sorted(pstr) == full:
                print("found", pstr)
                found.append(pstr)

    print(found)
    print(sorted(found)[-1])


pandig(10**5)
