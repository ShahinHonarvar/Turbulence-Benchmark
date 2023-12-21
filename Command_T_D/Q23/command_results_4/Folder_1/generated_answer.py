def find_divisors_in_range(n):
    if n <= 1:
        return []
    for x in range(10, n//2 + 1):
        if n % x == 0:
            yield x
    for x in range(n//2, n + 1):
        if n % x == 0:
            yield x
