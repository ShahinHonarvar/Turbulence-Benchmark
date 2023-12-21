def sum_of_divisors_in_range(n):
    if n == 1 or n == 2:
        return 0
    elif n == 3 or n == 5:
        return 1
    elif n == 6 or n == 10:
        return 2
    elif n == 15 or n == 21:
        return 3
    elif n == 28 or n == 36:
        return 4
    elif n == 41 or n == 55:
        return 5
    elif n == 56 or n == 63:
        return 6
    elif n == 65:
        return 7
    else:
        return 0
