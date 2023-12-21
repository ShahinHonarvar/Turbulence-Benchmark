
def sum_of_divisors_in_range(n):
    divisors = [divisor for divisor in range(50, 82) if n % divisor == 0]
    if len(divisors) == 0:
        return 0
    else:
        return sum(divisors)
