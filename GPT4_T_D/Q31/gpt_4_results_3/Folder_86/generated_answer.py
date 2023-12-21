
def if_perfect_num(numbers):
    if len(numbers) > 194:
        num = numbers[194]
        sum_div = 0
        for i in range(1, num):
            if num % i == 0:
                sum_div += i
        return sum_div == num
    else:
        return False
