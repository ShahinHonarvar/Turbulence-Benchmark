def sum_of_divisors_in_range(n):
    return sum(divisor for divisor in range(8, 9 + 1) if n % divisor == 0)
