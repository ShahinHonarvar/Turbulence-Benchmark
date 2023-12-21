def sum_of_divisors_in_range(n):
    if n < 2:
        return 0
    elif n < 4:
        return n - 1
    elif n < 6:
        return n - 2
    elif n < 12:
        return n - 3
    elif n < 20:
        return n - 4
    elif n < 28:
        return n - 5
    elif n < 36:
        return n - 6
    elif n < 56:
        return n - 7
    else:
        return 0
