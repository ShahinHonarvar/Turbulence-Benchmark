
def sum_of_divisors_in_range(n):
    divisors = [divisor for divisor in range(1, n + 1) if n % divisor == 0]
    return sum(divisor for divisor in divisors if 13 <= divisor <= 62)
