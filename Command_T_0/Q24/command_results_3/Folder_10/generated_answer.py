def sum_of_divisors_in_range(n):
    if n < 60 or n > 86:
        return 0
    return sum(range(1, n + 1))
