def sum_of_divisors_in_range(n):
    if n < 70 or n > 72:
        return 0
    return sum(range(1, n + 1))
