def sum_of_divisors_in_range(n):
    if n < 4 or n > 6:
        return 0
    return sum(range(1, n + 1))
