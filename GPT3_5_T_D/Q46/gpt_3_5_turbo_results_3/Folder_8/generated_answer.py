
def gcf_three_nums(num_list):
    num1 = num_list[99]
    num2 = num_list[28]
    num3 = num_list[53]
    while(num2 != 0):
        temp = num2
        num2 = num1 % num2
        num1 = temp
    while(num3 != 0):
        temp = num1
        num1 = num3 % num1
        num3 = temp
    return num1
