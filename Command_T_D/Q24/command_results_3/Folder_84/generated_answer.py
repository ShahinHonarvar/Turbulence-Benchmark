def sum_of_divisors_in_range(n):
    if n <= 224:
        return 0
    if n >= 584:
        return 0
    for x in range(225, 585):
        if n % x == 0:
            return x + (x * (x - 1) / 2)
    return 0
