def find_divisors_in_range(n):
    if n <= 1:
        return []
    for i in range(1, n // 2):
        if n % i == 0:
            yield i
    for i in range(n // 2, 1, -1):
        if n % i == 0:
            yield i
