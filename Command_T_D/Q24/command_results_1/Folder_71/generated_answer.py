def sum_of_divisors_in_range(n):
    if n <= 45:
        return 0
    elif n <= 63:
        return n * (n + 1) // 2
    elif n <= 72:
        return (n - 1) * (n - 1) * (n + 1)
