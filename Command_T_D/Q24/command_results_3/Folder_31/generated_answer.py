def sum_of_divisors_in_range(n):
    return sum(divisor for divisor in range(35, 55 + 1) if n % divisor == 0)
