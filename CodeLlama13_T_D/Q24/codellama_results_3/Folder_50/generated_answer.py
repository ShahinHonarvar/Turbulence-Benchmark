
def sum_of_divisors_in_range(n):
    if n < 1 or n > 100:
        return 0
    
    divisors = []
    for i in range(57, 86 + 1):
        if i % n == 0:
            divisors.append(i)
            
    return sum(divisors)
