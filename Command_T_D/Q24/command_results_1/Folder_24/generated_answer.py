def sum_of_divisors_in_range(n):
    if n < 43 or n > 95:
        return 0
    divisor_sum = 1
    for i in range(2, 1 + int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            divisor_sum += i + n // i
    return divisor_sum
