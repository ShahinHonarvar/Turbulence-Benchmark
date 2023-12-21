
def sum_of_divisors_in_range(n):
    divisors = [i for i in range(1, n+1) if n % i == 0]
    sum = 0
    
    for divisor in divisors:
        if 4 <= divisor <= 6:
            sum += divisor
    
    return sum
