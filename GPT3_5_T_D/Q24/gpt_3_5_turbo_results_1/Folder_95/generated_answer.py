
def sum_of_divisors_in_range(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    divisors_in_range = [divisor for divisor in divisors if 35 <= divisor <= 98]
    return sum(divisors_in_range) if divisors_in_range else 0
