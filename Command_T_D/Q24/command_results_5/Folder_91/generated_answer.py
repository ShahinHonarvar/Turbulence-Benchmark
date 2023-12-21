def sum_of_divisors_in_range(n):
    return sum(range(2, min(10, n//2) + 1, 2))
