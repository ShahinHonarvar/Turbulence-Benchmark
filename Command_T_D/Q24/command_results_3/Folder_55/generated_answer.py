def sum_of_divisors_in_range(n):
    if n <= 4:
        return 0
    else:
        return n * (n + 1) // 2
