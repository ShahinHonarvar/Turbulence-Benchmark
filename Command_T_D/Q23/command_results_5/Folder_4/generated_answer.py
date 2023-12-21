def find_divisors_in_range(n):
    if n <= 47 or n >= 61:
        return []
    for i in range(48, 60):
        if n % i == 0:
            yield i
            if n != i * i:
                yield n // i
    yield n
