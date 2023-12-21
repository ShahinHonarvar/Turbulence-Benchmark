def find_divisors_in_range(n):
    if n < 6:
        return []
    for i in range(3, n // 2 + 1):
        if n % i == 0:
            yield i
    for i in range(3, n // 2 + 1):
        if n % (i + 1) == 0:
            yield i + 1
