def find_divisors_in_range(n):
    for i in range(58, 90 + 1):
        if n % i == 0:
            yield i
    if n == 1:
        yield 1
    for i in range(2, n // 2 + 1):
        for j in range(i + 1, n // i + 1):
            yield i * j
