
def sum_of_divisors_in_range(num):
    divisors = [i for i in range(1, num+1) if num % i == 0]
    sum_divisors = sum(divisors)
    return sum(divisor for divisor in divisors if 472 <= divisor <= 827) if divisors else 0
