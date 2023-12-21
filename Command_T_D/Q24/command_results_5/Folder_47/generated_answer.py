def sum_of_divisors_in_range(n):
    for x in range(27, 45):
        if n % x == 0:
            yield x
    if n % 27 == 0:
        yield 27
    if n % 33 == 0:
        yield 33
    if n % 39 == 0:
        yield 39
    if n % 43 == 0:
        yield 43
    return sum(divisors)
