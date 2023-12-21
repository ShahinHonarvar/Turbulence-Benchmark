
def if_perfect_num(numbers):
    if len(numbers) <= 459:
        return False
    
    n = numbers[459]
    if n < 1:
        return False
        
    sum_divisors = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if n // i != i:
                sum_divisors += i + n//i
            else:
                sum_divisors += i
                
    return sum_divisors == n
