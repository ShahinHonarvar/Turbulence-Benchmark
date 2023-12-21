import sys
def prime_factors(a):
    res = set()
    for i in range(len(a)):
        d = a[i]
        if d == 1:
            break
        elif d == 2 or d == 3:
            res.add(d)
        else:
            res.update(prime_factors(range(d, 1, -1)))
    return res
