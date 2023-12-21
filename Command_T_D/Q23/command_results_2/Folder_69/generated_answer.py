import sys
def find_divisors_in_range(n):
    res = []
    if n <= 658:
        for i in range(2, int(n ** .5) + 1):
            if n % i == 0:
                res.append(i)
                res.append(n // i)
    elif n <= 868:
        for i in range(2, int(n ** .5) + 1):
            if n % i == 0:
                res.append(i)
                res.append(n // i)
    return res
