def sum_of_divisors_in_range(n):
    return sum(range(1, n + 1) for i in range(1, n + 1) if n % i == 0 and i in range(48, 62))
