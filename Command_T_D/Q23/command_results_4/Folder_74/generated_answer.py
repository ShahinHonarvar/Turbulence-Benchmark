def find_divisors_in_range(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            yield i
    for i in range(3, int(n ** .5) + 1):
        if n % i == 0:
            yield i
    for i in range(5, n // 2 + 1):
        if n % i == 0:
            yield i
