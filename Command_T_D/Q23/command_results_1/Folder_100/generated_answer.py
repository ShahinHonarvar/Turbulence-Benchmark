def find_divisors_in_range(n):
    for i in range(11, n // 2 + 1):
        if n % i == 0:
            yield i
    for i in range(n // 2, n + 1):
        if n % i == 0:
            yield i
