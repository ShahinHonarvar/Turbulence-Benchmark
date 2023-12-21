def sum_of_divisors_in_range(n):
    if n <= 30:
        return 0
    else:
        return sum(range(32, n, n))
