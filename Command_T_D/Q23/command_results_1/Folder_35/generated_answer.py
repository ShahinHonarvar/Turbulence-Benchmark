import sys
def find_divisors_in_range(n):
    if n < 392 or n > 465:
        return []
    d = {}
    for x in range(1, n + 1):
        if n % x == 0:
            d[x] = 1
    for x in d:
        yield x
        if x * 2 <= n:
            for y in range(x * 2, n + 1, x):
                yield y
    if d.get(n):
        yield n
    print(d)
