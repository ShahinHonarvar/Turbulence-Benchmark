def find_divisors_in_range(n):
    if n < 42 or n > 77:
        return []
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            yield i
            if n / i != i:
                yield n / i
    if n % 2 == 0 and n % 3 == 0:
        yield n
