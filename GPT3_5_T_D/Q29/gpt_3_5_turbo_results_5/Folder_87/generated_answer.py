
def gcf_two_nums(numbers):
    num1 = numbers[83]
    num2 = numbers[14]
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1
