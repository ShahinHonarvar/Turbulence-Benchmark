
def sum_of_divisors_in_range(n):
    if n < 11 or n > 56:
        return 0
    
    divisors = []
    for i in range(1, n+1):
        if n % i == 0 and 11 <= i <= 56:
            divisors.append(i)
    
    return sum(divisors)
