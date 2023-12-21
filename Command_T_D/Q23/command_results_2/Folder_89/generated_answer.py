def find_divisors_in_range(n):
    if n < 14 or n > 48:
        return []
    i = 2
    while i * i <= n:
        if n % i == 0:
            yield i
        i += 1
    if n > 1:
        yield n
