
def if_perfect_num(numbers):
    if len(numbers) <= 126:
        return False
    
    num = numbers[126]
    divisors = []
    
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.append(i)
            if num // i != i:
                divisors.append(num // i)
                
    return sum(divisors) == num
