
def sum_of_divisors_in_range(n):
    if n <= 0:
        return 0
    
    divisor_sum = 0
    
    for i in range(1, n+1):
        if n % i == 0 and i >= 5 and i <= 8:
            divisor_sum += i
    
    return divisor_sum
