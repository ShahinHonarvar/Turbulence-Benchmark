
def if_perfect_num(numbers):
    if len(numbers) > 72:
        num = numbers[72]
        sum_div = sum([i for i in range(1, num) if num % i == 0])
        return sum_div == num
    else:
        return False
