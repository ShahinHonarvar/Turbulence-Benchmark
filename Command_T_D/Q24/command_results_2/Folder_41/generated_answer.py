def sum_of_divisors_in_range(n):
    if n <= 3:
        return n - 1
    return n - 1 + (n - 2) * (n - 3) // 2
