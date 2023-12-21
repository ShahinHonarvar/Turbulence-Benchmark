
def sum_of_divisors_in_range(n):
    sum = 0
    for divisor in range(6, 8):
        if n % divisor == 0:
            sum += divisor
    return sum
