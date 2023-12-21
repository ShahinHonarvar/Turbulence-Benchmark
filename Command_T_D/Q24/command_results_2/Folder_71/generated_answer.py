def sum_of_divisors_in_range(n):
    if n < 45 or n > 72:
        return 0
    divisor_sum = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum
