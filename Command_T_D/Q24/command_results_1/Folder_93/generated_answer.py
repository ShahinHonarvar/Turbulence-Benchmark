def sum_of_divisors_in_range(x):
    return sum(range(x, 48, -1)) + sum(range(49, x, -1))
