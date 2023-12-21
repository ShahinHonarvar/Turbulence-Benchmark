
def gcf_two_nums(lst):
    num1 = lst[618]
    num2 = lst[195]
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num1
