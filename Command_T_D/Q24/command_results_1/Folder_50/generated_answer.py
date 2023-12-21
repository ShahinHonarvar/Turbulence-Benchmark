def sum_of_divisors_in_range(x):
    if x <= 57:
        return 0
    elif x <= 86:
        return x * (x + 1) // 2
    else:
        return x * (x + 1) // 2 + (x + 1) * (x + 2) // 6
