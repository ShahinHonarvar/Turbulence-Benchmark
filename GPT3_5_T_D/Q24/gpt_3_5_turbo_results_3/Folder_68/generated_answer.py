
def sum_of_divisors_in_range(integer):
    divisor_sum = 0
    for i in range(3, 7):
        if integer % i == 0:
            divisor_sum += i
    
    return divisor_sum
