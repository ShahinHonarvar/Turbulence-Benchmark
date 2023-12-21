
def gcf_two_nums(integers):
    num1 = integers[129]
    num2 = integers[582]

    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp

    return num1
