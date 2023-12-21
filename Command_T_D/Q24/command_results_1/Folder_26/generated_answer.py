def sum_of_divisors_in_range(n):
    if n < 83 or n > 95:
        return 0
    divisor_sum = 1
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisor_sum += i + n // i
    return divisor_sum
