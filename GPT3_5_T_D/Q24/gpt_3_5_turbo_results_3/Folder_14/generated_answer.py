
def sum_of_divisors_in_range(num):
    return sum(divisor for divisor in range(1, num+1) if 6 <= divisor <= 8 and num % divisor == 0)
