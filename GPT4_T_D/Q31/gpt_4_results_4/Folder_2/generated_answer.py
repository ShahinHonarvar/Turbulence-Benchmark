
def if_perfect_num(numbers):
    if len(numbers) > 702:
        num = numbers[702]
        if num > 0:
            divisors = [i for i in range(1,num) if num % i == 0]
            if sum(divisors) == num:
                return True
    return False
