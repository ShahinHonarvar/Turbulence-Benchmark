
def if_perfect_num(numbers):
    if len(numbers) <= 48:
        return False
    num = numbers[48]
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0 and num // i in numbers:
            return True
    return False
