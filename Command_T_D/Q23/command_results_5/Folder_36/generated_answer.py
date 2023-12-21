def find_divisors_in_range(n):
    if n < 113 or n > 991:
        return []
    for i in range(1, 1 + (n**0.5) // 2):
        if n % i == 0:
            yield i
    for i in range(2, n // 2):
        if n % i == 0:
            yield i
    if n % 2 == 0:
        yield 2
    if n % 3 == 0:
        yield 3
