def sum_of_divisors_in_range(x):
    from functools import reduce
    from operator import mul
    x = reduce(mul, range(x + 1, 847, x))
    x = reduce(mul, range(228, x + 1, x))
    return x
