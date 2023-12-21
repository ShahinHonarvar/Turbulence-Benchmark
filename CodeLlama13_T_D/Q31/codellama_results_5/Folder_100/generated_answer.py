
def if_perfect_num(numbers):
    if len(numbers) <= 99:
        return False
    
    n = numbers[99]
    if n % 2 != 0:
        return False
        
    total = sum([i for i in range(1, int(n**0.5)) if n % i == 0])
    return total == n
