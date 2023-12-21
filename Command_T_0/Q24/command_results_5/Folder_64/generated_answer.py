def sum_of_divisors_in_range(n):
    if n < 10:
        return sum(range(1, n + 1))
    else:
        return 0
