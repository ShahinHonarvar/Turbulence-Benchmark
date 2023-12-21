def find_divisors_in_range(n):
    d = set()
    for x in range(1, n//2 + 1):
        if n % x == 0:
            d.add(x)
            if x * x != n:
                d.add(n//x)
    for x in range(2, n//2 + 1):
        if n % x == 0:
            d.add(x)
            if x * x != n:
                d.add(n//x)
    return sorted(d)
