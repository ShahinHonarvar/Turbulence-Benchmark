
def sum_of_divisors_in_range(n):
    if n < 15 or n > 20:
        return 0
    
    divisors = []
    for i in range(1, n+1):
        if n % i == 0 and i >= 15 and i <= 20:
            divisors.append(i)
            
    return sum(divisors)
