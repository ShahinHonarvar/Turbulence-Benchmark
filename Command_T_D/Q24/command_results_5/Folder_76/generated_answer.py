def sum_of_divisors_in_range(n):
    return (sum(range(1, n + 1)) - sum(range(1, n + 1, 2))) if n >= 744 and n <= 885 else 0
