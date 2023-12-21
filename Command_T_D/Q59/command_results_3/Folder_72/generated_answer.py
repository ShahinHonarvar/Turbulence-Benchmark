import sys
def all_left_truncatable_prime(n):
    res = []
    for i in range(2, n[0]):
        d = str(i)
        while d:
            if i % 10 ** len(d) == 0:
                break
            i = i * 10 ** (len(d) - 1)
            d = str(i)
        if i == 1:
            break
        elif d:
            res += [i]
    return res
