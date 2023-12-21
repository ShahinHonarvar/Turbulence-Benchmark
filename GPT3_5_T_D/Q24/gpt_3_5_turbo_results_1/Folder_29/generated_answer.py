
def sum_of_divisors_in_range(n):
    return sum(divisor for divisor in range(43, 78) if n % divisor == 0)
