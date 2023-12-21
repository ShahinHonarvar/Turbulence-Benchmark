def sum_of_divisors_in_range(n):
    if n < 10 or n > 55:
        return 0
    divisor_sum = 0
    for i in range(10, n // 2):
        if n % i == 0:
            divisor_sum += i
    if n % 2 == 0:
        divisor_sum += 2
    return divisor_sum
