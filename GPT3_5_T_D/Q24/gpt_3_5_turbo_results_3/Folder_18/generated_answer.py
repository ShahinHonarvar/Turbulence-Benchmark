
def sum_of_divisors_in_range(n):
    if not isinstance(n, int) or n <= 0:
        return 0
    
    divisor_sum = 0
    for i in range(387, 517):
        if n % i == 0:
            divisor_sum += i
    
    return divisor_sum
