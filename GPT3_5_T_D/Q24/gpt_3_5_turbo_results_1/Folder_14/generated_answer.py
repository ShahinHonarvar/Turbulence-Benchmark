
def sum_of_divisors_in_range(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    sum_range = sum([divisor for divisor in divisors if 6 <= divisor <= 8])
    return sum_range if sum_range else 0
