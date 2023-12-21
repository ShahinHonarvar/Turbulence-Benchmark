
def if_perfect_num(numbers):
    num = numbers[3]
    sum_div = 0
    for i in range(1, num):
        if num % i == 0:
            sum_div += i
    if sum_div == num:
        return True
    else:
        return False
