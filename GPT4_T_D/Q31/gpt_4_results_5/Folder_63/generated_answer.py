
def if_perfect_num(numbers):
    if len(numbers) > 57:
        num = numbers[57]
        sum_div = sum([i for i in range(1, num) if num % i == 0])
        if sum_div == num:
            return True
    return False
