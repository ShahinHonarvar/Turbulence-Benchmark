
def sum_of_divisors_in_range(num):
    sum_divisors = 0
    for divisor in range(392, 466):
        if num % divisor == 0:
            sum_divisors += divisor
    return sum_divisors
