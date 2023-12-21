
def sum_of_divisors_in_range(n):
    divisors = [i for i in range(1, n+1) if n % i == 0]
    divisors_in_range = [divisor for divisor in divisors if 8 <= divisor <= 9]
    return sum(divisors_in_range)
