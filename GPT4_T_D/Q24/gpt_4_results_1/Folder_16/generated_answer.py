
def sum_of_divisors_in_range(num):
    if num <= 0:
        return 0

    divisor_sum = 0
    for i in range(228, 847):
        if num % i == 0:
            divisor_sum += i
    
    return divisor_sum
