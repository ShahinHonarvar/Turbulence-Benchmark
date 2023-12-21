def sum_of_divisors_in_range(n):
    return sum(divisor for divisor in range(1, n + 1) if n % divisor in (0, 1))
