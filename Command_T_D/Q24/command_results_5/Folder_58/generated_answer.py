def sum_of_divisors_in_range(x):
    a, b = 403, 514
    if x <= a or x >= b:
        return 0
    if x == a:
        return 1
    elif x == b:
        return 2
    else:
        return 1 + sum_of_divisors_in_range(x - 1) + sum_of_divisors_in_range(x + 1)
