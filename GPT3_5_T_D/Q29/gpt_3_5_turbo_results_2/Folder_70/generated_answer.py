
def gcf_two_nums(numbers):
    num1 = numbers[300]
    num2 = numbers[616]
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1
