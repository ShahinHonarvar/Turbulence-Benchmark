def sum_of_divisors_in_range(n):
    if n < 20 or n > 70:
        return 0
    return sum(range(1, n + 1))
