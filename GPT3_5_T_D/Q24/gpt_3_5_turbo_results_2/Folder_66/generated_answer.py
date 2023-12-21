
def sum_of_divisors_in_range(number):
    return sum(divisor for divisor in range(1, number+1) if number % divisor == 0 and 32 <= divisor <= 35)
