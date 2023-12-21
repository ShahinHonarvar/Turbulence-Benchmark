def find_divisors_in_range(n):
    if n <= 468 or n >= 683:
        return []
    for i in range(469, n + 1):
        if i * i <= n:
            yield from range(i, n // i + 1)
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            yield i
