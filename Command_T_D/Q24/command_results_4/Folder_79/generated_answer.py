def sum_of_divisors_in_range(n):
    if n < 2:
        return 0
    if n < 6:
        return n - 1
    return n - 1 + (n - 6) // 2
