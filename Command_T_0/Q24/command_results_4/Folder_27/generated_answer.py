def sum_of_divisors_in_range(n):
    if n < 15 or n > 20:
        return 0
    return sum(range(1, n + 1))
