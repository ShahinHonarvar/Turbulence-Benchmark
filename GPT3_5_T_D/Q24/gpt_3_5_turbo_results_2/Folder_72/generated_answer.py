
def sum_of_divisors_in_range(n):
    return sum(divisor for divisor in range(1, n + 1) if 32 <= divisor <= 90 and n % divisor == 0) if n > 0 else 0
