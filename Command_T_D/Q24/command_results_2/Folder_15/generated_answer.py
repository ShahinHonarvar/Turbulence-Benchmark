def sum_of_divisors_in_range(n):
    if n < 8:
        return 0
    return sum(x for x in range(7, n // 2 + 1) if n % x == 0)
