
def sum_of_divisors_in_range(num):
    divisors = [divisor for divisor in range(1, num+1) if num % divisor == 0]
    divisors_between_3_and_5 = [divisor for divisor in divisors if 3 <= divisor <= 5]
    return sum(divisors_between_3_and_5)
