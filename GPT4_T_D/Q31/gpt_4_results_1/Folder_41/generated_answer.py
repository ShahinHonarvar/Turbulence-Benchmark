
def if_perfect_num(numbers):
    if len(numbers) <= 84:
        return False
    
    num = numbers[84]
    divisors = [x for x in range(1, num) if num % x == 0]

    return sum(divisors) == num
