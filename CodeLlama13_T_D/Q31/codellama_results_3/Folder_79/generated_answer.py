
def if_perfect_num(numbers):
    if len(numbers) <= 63:
        return False
    else:
        num = numbers[63]
        for i in range(1, num // 2 + 1):
            if num % i == 0 and i * (num // i) == num:
                return True
        return False
