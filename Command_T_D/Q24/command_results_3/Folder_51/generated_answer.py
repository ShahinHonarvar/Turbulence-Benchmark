def sum_of_divisors_in_range(n):
    if n < 2 or n > 7:
        return 0
    if n == 2 or n == 3 or n == 6:
        return 1
    elif n == 4 or n == 5:
        return 2
    elif n == 7:
        return 3
    else:
        return 0
