
def gcf_two_nums(lst):
    num1 = lst[184]
    num2 = lst[307]
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num1
