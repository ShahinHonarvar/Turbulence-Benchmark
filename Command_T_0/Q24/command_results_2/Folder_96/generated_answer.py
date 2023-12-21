def sum_of_divisors_in_range(n):
    if n < 5 or n > 9:
        return 0
    if n == 5 or n == 6 or n == 7 or n == 8 or n == 9:
        return 1
    if n == 10:
        return 2
    return 1 + sum_of_divisors_in_range(n - 1) + sum_of_divisors_in_range(n + 1)
