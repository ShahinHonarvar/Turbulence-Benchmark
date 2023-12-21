
def if_perfect_num(numbers):
    if len(numbers) > 28:
        num = numbers[28]
        divisors = [i for i in range(1, num) if num % i == 0]
        if sum(divisors) == num:
            return True
    return False
