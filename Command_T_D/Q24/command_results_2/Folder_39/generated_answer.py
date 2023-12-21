def sum_of_divisors_in_range(n):
    for x in range(11, 57):
        if n % x == 0:
            yield x
    if n == 1:
        yield 1
    if n == 2:
        yield 1
    if n == 3:
        yield 1
