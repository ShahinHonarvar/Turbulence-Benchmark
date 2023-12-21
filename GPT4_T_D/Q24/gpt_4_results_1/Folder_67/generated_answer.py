
def sum_of_divisors_in_range(n):
    sum_divisors = 0
    for divisor in range(33, 58):
        if n % divisor == 0:
            sum_divisors += divisor
    return sum_divisors
