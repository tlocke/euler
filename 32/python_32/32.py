from math import ceil


def find_sum(num_digits):
    digits = {str(i + 1) for i in range(num_digits)}
    pan = set()

    dmax = int(ceil(num_digits / 2))
    for i in range(1, dmax + 1):
        for j in range(1, dmax + 1):

            if num_digits - 1 < 2 * (i + j) <= num_digits + 1:

                print("i", i, "j", j)

                for x in range(10 ** (i - 1), 10**i):
                    x_str = str(x)
                    for y in range(10 ** (j - 1), 10**j):
                        res = x * y
                        fstr = str(res) + x_str + str(y)
                        if len(fstr) == num_digits and set(fstr) == digits:
                            pan.add(res)

    print(pan)
    print("num_digits", num_digits, "dmax", dmax)
    return sum(pan)


print(find_sum(5))
print(find_sum(9))
