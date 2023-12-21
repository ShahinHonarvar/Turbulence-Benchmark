
def if_perfect_num(numbers):
    if len(numbers) > 35:
        num = numbers[35]
        factors = [i for i in range(1, num) if num % i == 0]
        if sum(factors) == num:
            return True
        else:
            return False
    else:
        return False
