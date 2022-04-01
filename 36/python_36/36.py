def is_p(x):
    return x == "".join(reversed(x))


def find_tot(m):
    tot = 0
    for i in range(m):
        dec_str = str(i)
        bin_str = bin(i)[2:]
        if is_p(dec_str) and is_p(bin_str):
            print("found", dec_str, bin_str)
            tot += i
    print(tot)


find_tot(1000000)
