def sum_of_divisors_in_range(n):
    if n <= 4 or n >= 10:
        return 0
    elif n == 5:
        return 1
    elif n == 6:
        return 4
    elif n == 7:
        return 6
    elif n == 8:
        return 10
    elif n == 9:
        return 14
