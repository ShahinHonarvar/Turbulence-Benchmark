def sum_of_divisors_in_range(n):
    return sum(divisor for divisor in range(48, n // 2, n // 2) if n % divisor == 0)
