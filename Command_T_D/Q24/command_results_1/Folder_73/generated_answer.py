def sum_of_divisors_in_range(n):
    divisor_sum = 0
    for x in range(46, 89):
        if n % x == 0:
            divisor_sum += x
    return divisor_sum
