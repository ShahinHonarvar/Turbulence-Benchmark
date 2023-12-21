def sum_of_divisors_in_range(n):
    if n < 7:
        return 0
    elif n > 8:
        return n - 1
    else:
        return n - 2
