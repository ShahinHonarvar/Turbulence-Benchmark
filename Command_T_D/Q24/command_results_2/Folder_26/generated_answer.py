def sum_of_divisors_in_range(n):
    if n < 83 or n > 95:
        return 0
    divisor_sum = 0
    for i in range(1, 1 + int(n**0.5)):
        if n % i == 0:
            divisor_sum += i + n // i
    if n ** 0.5 % 1 == 0:
        divisor_sum += n ** 0.5
    return divisor_sum
