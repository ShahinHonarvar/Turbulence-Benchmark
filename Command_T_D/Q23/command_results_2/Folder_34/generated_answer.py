def find_divisors_in_range(n):
    if n < 4 or n > 5:
        return []
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            yield i
    for i in range(int(n ** .5) + 1, n // 2 + 1):
        if n % i == 0:
            yield i
