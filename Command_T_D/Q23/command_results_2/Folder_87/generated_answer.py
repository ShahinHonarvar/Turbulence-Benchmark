def find_divisors_in_range(n):
    if n < 50 or n > 81:
        return []
    for i in range(2, n + 1):
        if n % i == 0:
            yield i
    for i in range(3, int(n ** .5) + 1):
        if n % i == 0:
            yield i
    for i in range(5, int(n ** .5) + 1):
        if n % i == 0:
            yield i
