
def if_perfect_num(numbers):
    if len(numbers) <= 99:
        return False
    
    num = numbers[99]
    divisors = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.add(i)
            if i * i != num:
                divisors.add(num // i)
    
    return sum(divisors) == num
