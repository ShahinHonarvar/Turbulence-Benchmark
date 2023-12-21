
def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    sum_of_divisors = 0
    for divisor in divisors:
        if 4 <= divisor <= 8:
            sum_of_divisors += divisor
    return sum_of_divisors
