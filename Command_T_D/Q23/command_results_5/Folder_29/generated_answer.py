def find_divisors_in_range(n):
    if n < 43 or n > 77:
        return []
    for i in range(2, int(n**(0.5)) + 1):
        if n % i == 0:
            yield i
            for j in range(2, int(n / i) + 1):
                if n % j == 0:
                    yield j
    if n > 1:
        yield n
