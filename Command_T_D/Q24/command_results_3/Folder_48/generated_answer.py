def sum_of_divisors_in_range(x):
    if x > 827:
        return 0
    if x <= 461:
        return 0
    if x == 828:
        return 0
    return sum(range(x, 828, x))
