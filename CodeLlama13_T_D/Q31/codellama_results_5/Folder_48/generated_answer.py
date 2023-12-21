
def if_perfect_num(numbers):
    if len(numbers) <= 247:
        return False
    else:
        num = numbers[247]
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0 and num // i == i:
                return True
        return False
