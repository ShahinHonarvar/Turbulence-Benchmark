def sum_of_divisors_in_range(n):
    if n < 15:
        return 0
    for i in range(14, n // 2 + 1):
        if n % i == 0:
            if i == n // i:
                continue
            yield i
    if n % 2 == 0:
        yield 2
    for i in range(3, int(n ** .5) + 1):
        if n % i == 0:
            if i == n // i:
                continue
            yield i
