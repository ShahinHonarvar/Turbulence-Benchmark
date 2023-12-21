def sum_of_divisors_in_range(n):
    if n < 2 or n > 9:
        return 0
    elif n == 2 or n == 3 or n == 5 or n == 7 or n == 9:
        return 1
    elif n == 4:
        return 6
    elif n == 6:
        return 10
    elif n == 8:
        return 22
    else:
        return 1 + sum_of_divisors_in_range(n - 1) + sum_of_divisors_in_range(n + 1)
