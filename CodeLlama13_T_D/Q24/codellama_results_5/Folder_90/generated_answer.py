
def sum_of_divisors_in_range(n):
    if n <= 450 or n >= 974:
        return 0
    
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0 and i >= 451 and i <= 973:
            divisors.append(i)
            
    return sum(divisors)
