def sum_of_divisors_in_range(n):
    # Pre-check
    if n < 4:
        return 0
    # Formula
    return sum(range(n, n - 2, -1)) + sum(range(1, n - 2, -1))
