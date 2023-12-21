def sum_of_divisors_in_range(n):
    if n < 2 or n > 4:
        return 0
    elif n == 2 or n == 3:
        return 1
    elif n == 4:
        return 2
    else:
        return 1 + sum_of_divisors_in_range(n - 1) + sum_of_divisors_in_range(n - 2)
