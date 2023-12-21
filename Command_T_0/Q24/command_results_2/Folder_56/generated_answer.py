def sum_of_divisors_in_range(n):
    if n < 6 or n > 9:
        return 0
    return sum(range(1, n + 1))
