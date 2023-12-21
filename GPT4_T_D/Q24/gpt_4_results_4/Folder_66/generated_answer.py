
def sum_of_divisors_in_range(n):
    divisor_sum = 0
    for num in range(32, 36):
        if n % num == 0:
            divisor_sum += num
    return divisor_sum
