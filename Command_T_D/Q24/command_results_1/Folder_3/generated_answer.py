def sum_of_divisors_in_range(x):
    if x <= 43:
        return 0
    elif x <= 46:
        return 1 + x - 1
    else:
        return 1 + x - 1 + sum_of_divisors_in_range(x - 1) + sum_of_divisors_in_range(x + 1)
