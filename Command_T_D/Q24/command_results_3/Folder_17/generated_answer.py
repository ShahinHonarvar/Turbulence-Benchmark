def sum_of_divisors_in_range(n):
    if n <= 10 or n >= 70:
        return 0
    return sum(d for d in range(10, n, 1) if n % d == 0)
