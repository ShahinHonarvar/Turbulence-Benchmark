
def sum_of_divisors_in_range(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    divisors_in_range = [divisor for divisor in divisors if 83 <= divisor <= 95]
    return sum(divisors_in_range) if divisors_in_range else 0
