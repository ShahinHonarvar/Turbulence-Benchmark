
def sum_of_divisors_in_range(n):
    if n <= 0:
        return 0
    
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    
    sum = 0
    for divisor in divisors:
        if 378 <= divisor <= 782:
            sum += divisor
    
    return sum
