def find_divisors_in_range(n):
    if n <= 4 or n >= 10:
        return []
    for i in range(5, n // 2 + 1):
        if n % i == 0:
            yield i
    for i in range(n // 2, n // 3 + 1):
        if n % i == 0:
            yield i
