
def if_perfect_num(numbers):
    if len(numbers) <= 74:
        return False
    else:
        num = numbers[74]
        for i in range(1, num // 2 + 1):
            if num % i == 0 and i ** 2 == num:
                return True
        return False
