def sum_of_divisors_in_range(n):
    if n < 2:
        return 0
    else:
        return (n - 1) * (n - 1) // 2
