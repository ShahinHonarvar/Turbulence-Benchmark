
def if_perfect_num(numbers):
    if len(numbers) > 60:
        num = numbers[60]
        if num > 1:
            divisors = [i for i in range(1,num) if num % i == 0]
            if sum(divisors) == num:
                return True
    return False
