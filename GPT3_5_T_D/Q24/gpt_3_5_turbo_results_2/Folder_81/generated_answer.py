
def sum_of_divisors_in_range(integer):
    divisors = [divisor for divisor in range(3, integer+1) if integer % divisor == 0]
    divisors_in_range = [divisor for divisor in divisors if divisor >= 3 and divisor <= 4]
    return sum(divisors_in_range) if divisors_in_range else 0
