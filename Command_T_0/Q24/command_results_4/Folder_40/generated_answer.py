def sum_of_divisors_in_range(n):
    if n <= 1:
        return 0
    elif n <= 2:
        return 1
    else:
        return sum_of_divisors_in_range(n - 1) + sum_of_divisors_in_range(n - 2)
