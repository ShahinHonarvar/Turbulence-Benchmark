
def if_perfect_num(numbers):
    if len(numbers) <= 23:
        return False
    else:
        num = numbers[23]
        for i in range(1, int(sqrt(num)) + 1):
            if num % i == 0 and (i * i != num or i ** 2 != num):
                return True
        return False
