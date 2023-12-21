
def sum_of_divisors_in_range(n):
    divisors = [x for x in range(1, n+1) if n % x == 0]
    result = 0
    for divisor in divisors:
        if 4 <= divisor <= 8:
            result += divisor
    return result
