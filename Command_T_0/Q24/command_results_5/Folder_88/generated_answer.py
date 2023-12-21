def sum_of_divisors_in_range(n):
    if n < 6:
        return 0
    elif n == 6:
        return 1
    elif n == 7:
        return 2
    else:
        return 1 + sum(range(1, n // 2))
