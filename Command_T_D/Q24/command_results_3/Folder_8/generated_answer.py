def sum_of_divisors_in_range(n):
    if n <= 48 or n >= 62:
        return 0
    return n * (n + 1) // 2
