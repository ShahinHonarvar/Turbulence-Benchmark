
def if_perfect_num(numbers):
    if len(numbers) <= 48:
        return False
    
    number = numbers[48]
    divisors = []
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if number // i != i:
                divisors.append(number // i)
    
    return sum(divisors) == number
