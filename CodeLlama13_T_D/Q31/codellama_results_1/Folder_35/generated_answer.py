
def if_perfect_num(numbers):
    if len(numbers) <= 993:
        return False
    
    num = numbers[993]
    divisors = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if num // i != i:
                divisors.append(num // i)
    
    return sum(divisors) == num
