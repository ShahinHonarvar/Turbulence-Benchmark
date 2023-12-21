def sum_of_divisors_in_range(n):
    result = 0
    for divisor in range(14, 93 + 1):
        if n % divisor == 0:
            result += divisor
    return result
