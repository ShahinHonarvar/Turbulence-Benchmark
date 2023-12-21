
def sum_of_divisors_in_range(n):
    divisors = []
    
    for i in range(1, 8):
        if n % i == 0:
            divisors.append(i)
    
    if len(divisors) == 0:
        return 0
    
    return sum(divisors)
