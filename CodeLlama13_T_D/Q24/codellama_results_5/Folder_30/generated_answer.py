
def sum_of_divisors_in_range(n):
    if n < 1 or n > 77:
        return 0
    
    result = 0
    for i in range(42, n+1):
        if i % n == 0 and i >= 42 and i <= 77:
            result += i
            
    return result
