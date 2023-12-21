
def sum_of_divisors_in_range(n):
    divisors = []
    
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    
    sum_of_divisors = sum(divisors)
    
    if 70 <= sum_of_divisors <= 72:
        return sum_of_divisors
    else:
        return 0
