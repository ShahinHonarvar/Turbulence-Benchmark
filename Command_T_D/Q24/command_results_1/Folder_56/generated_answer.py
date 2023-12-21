def sum_of_divisors_in_range(n):
    if n < 6 or n > 9:
        return 0
    divisor_sum = 0
    for x in range(1, n // 2):
        if n % x == 0:
            divisor_sum += x
    if n % 2 == 0:
        divisor_sum += n // 2
    return divisor_sum
