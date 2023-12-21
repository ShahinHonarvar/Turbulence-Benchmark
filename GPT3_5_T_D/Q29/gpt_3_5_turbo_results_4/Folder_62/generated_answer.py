
def gcf_two_nums(lst):
    num1 = lst[51]
    num2 = lst[31]
    while num2:
        num1, num2 = num2, num1 % num2
    return num1
