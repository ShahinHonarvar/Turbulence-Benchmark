def find_divisors_in_range(n):
    for i in range(13, 63):
        if n % i == 0:
            yield i
    if n > 1:
        yield n
