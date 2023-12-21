
def find_divisors_in_range(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    divisors_in_range = [divisor for divisor in divisors if 70 <= divisor <= 93]
    return divisors_in_range
