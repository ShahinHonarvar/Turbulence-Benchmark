def sum_of_divisors_in_range(n):
    return sum(range(81, n//2 + 1, n//2) + range(n//2 + 1, n, n//2))
