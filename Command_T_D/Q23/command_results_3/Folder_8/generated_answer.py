def find_divisors_in_range(n):
    if n < 48 or n > 62:
        return []
    for i in range(1, n // 2):
        if n % i == 0:
            yield i
    for i in range(1, n // 2):
        if n % (i + 1) == 0:
            yield i + 1
