
def sum_of_divisors_in_range(n):
    if n < 120 or n > 349:
        return 0
    
    divisors = []
    for i in range(1, n+1):
        if n % i == 0 and i >= 120 and i <= 349:
            divisors.append(i)
    
    return sum(divisors)
