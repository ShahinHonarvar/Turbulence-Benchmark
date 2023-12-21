def sum_of_divisors_in_range(x):
    if x < 469 or x > 682:
        return 0
    if x == 469 or x == 682:
        return x
    x = (x + 1) // 2
    if x == 1 or x == 2:
        return x
    else:
        return (x - 1) * x
