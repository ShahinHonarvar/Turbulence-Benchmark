
def gcf_two_nums(lst):
    num1 = lst[28]
    num2 = lst[53]
    while num2:
        num1, num2 = num2, num1 % num2
    return num1
