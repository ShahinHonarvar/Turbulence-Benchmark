def sum_of_divisors_in_range(x):
    if x < 2:
        return 0
    if x <= 4:
        return (x / 2) * (x / 3)
    return (x / 2) * (x / 3) + (x / 3)
