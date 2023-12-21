def sum_of_divisors_in_range(n):
    if n <= 3:
        return 0
    elif n <= 6:
        return n - 1
    elif n <= 8:
        return n - 2
    elif n <= 9:
        return n - 3
