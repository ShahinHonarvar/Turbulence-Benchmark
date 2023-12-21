
def sum_of_divisors_in_range(n):
    if n < 1:
        return 0
    
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0 and 1 <= i <= 2:
            divisors.append(i)
    
    return sum(divisors)
