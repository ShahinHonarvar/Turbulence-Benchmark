def find_divisors_in_range(n):
    if n < 15 or n > 92:
        return []
    for i in range(15, n // 2):
        if n % i == 0:
            yield i
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            yield i
