
def if_perfect_num(numbers):
    if len(numbers) > 15:
        number = numbers[15]
        sum_divisor = 0
        for i in range(1, number):
            if number % i == 0:
                sum_divisor += i
        if sum_divisor == number:
            return True
    return False
