def sum_of_divisors_in_range(n):
    for i in range(84, 86):
        if n % i == 0:
            yield i
    if n % 84 == 0:
        yield 84
    if n % 86 == 0:
        yield 86
    return sum(divisors)
