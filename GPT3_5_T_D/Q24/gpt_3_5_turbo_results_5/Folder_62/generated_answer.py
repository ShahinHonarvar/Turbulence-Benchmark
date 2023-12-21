
def sum_of_divisors_in_range(num):
    divisors = [i for i in range(1, num+1) if num % i == 0]
    divisors_in_range = [divisor for divisor in divisors if divisor >= 59 and divisor <= 88]
    return sum(divisors_in_range)
