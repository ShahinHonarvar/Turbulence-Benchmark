import sys
def find_divisors_in_range(n):
    res = []
    for x in range(1, int(n ** .5) + 1):
        if n % x == 0:
            res.append(x)
            if x * x != n:
                res.append(n // x)
    return res
