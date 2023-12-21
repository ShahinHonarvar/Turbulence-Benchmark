
def if_perfect_num(numbers):
    if len(numbers) > 312:
        num = numbers[312]
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        if num == sum:
            return True
        else:
            return False
    else:
        return False
