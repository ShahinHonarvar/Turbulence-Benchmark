
def sum_of_divisors_in_range(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    sum_of_divisors = sum([divisor for divisor in divisors if 10 <= divisor <= 55])
    return sum_of_divisors if sum_of_divisors > 0 else 0
