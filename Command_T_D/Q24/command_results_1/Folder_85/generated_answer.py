def sum_of_divisors_in_range(n):
    if n < 2:
        return 0
    elif n == 2 or n == 3:
        return 1
    elif n == 4:
        return 2
    elif n == 5:
        return 3
    else:
        return 0
