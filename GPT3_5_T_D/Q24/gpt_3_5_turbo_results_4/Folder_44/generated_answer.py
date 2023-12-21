
def sum_of_divisors_in_range(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    
    sum = 0
    for divisor in divisors:
        if 50 <= divisor <= 84:
            sum += divisor
    
    return sum
