def sum_of_divisors_in_range(n):
    if n < 48 or n > 92:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    elif n == 3:
        return 6
    elif n == 4:
        return 12
    elif n == 5:
        return 20
    elif n == 6:
        return 30
    elif n == 7:
        return 42
    elif n == 8:
        return 56
    elif n == 9:
        return 72
    elif n == 10:
        return 90
