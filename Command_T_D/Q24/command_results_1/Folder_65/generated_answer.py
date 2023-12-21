def sum_of_divisors_in_range(n):
    if n < 46 or n > 65:
        return 0
    return sum(range(1, n+1))
