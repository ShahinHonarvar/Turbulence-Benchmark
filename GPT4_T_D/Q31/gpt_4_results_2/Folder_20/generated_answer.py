
def if_perfect_num(numbers):
    if len(numbers) > 53:
        num = numbers[53]
        if num > 1:
            factors = [i for i in range(1, num) if num % i == 0]
            if sum(factors) == num:
                return True
    return False
