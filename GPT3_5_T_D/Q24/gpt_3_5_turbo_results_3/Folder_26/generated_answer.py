
def sum_of_divisors_in_range(n):
    if n < 83 or n > 95:
        return 0

    divisors = [i for i in range(1, n+1) if n % i == 0]

    sum_of_divisors = 0
    for divisor in divisors:
        if 83 <= divisor <= 95:
            sum_of_divisors += divisor

    return sum_of_divisors
