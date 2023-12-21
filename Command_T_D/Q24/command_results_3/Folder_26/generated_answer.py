def sum_of_divisors_in_range(n):
    if n < 83 or n > 95:
        return 0
    if n == 1:
        return 1
    if n == 2 or n == 3:
        return 2
    return n * (n + 1) // 2
