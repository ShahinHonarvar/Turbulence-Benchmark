def sum_of_divisors_in_range(n):
    return sum(d for d in range(16, 54) if n % d == 0)
