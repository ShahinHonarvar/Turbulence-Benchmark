def find_divisors_in_range(n):
    d = set()
    for x in range(11, n // 2):
        if n % x == 0:
            d.add(x)
    for x in range(1, n // 2):
        if n % x == 0:
            d.add(x)
    return list(d)
