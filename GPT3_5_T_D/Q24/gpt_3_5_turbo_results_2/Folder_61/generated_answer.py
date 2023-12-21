
def sum_of_divisors_in_range(n):
    if n < 2:
        return 0
    
    divisors_sum = 0
    for i in range(2, 4):
        if n % i == 0:
            divisors_sum += i
    
    return divisors_sum
