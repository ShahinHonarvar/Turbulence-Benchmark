
def sum_of_divisors_in_range(num):
    divisor_sum = 0
    for i in range(35, 56):
        if num % i == 0:
            divisor_sum += i
    return divisor_sum
