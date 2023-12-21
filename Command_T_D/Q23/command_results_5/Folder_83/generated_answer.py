def find_divisors_in_range(n):
    if n < 6:
        return []
    for i in range(5, 7):
        if n % i == 0:
            yield i
    for i in range(5, int(n**(0.5)) + 1):
        if n % i == 0:
            yield i
