def find_divisors_in_range(n):
    if n <= 3 or n >= 8:
        return []
    for i in range(4, n//2):
        if n % i == 0:
            yield i
    for i in range(3, int(n**0.5) + 1):
        if n % i == 0:
            yield i
    if n % 2 == 0:
        yield 2
    if n % 3 == 0:
        yield 3
