def sum_of_divisors_in_range(x):
    from functools import reduce
    return reduce(lambda a, b: a + b, (i for i in range(x, x + 100, 1) if x % i == 0))
