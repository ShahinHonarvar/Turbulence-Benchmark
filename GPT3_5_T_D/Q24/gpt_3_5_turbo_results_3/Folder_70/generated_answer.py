
def sum_of_divisors_in_range(n):
    divisors = [i for i in range(1, n+1) if n % i == 0]
    return sum(divisor for divisor in divisors if 586 <= divisor <= 840) if divisors else 0
