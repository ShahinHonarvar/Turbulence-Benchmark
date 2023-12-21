
def gcf_two_nums(lst):
    num1 = lst[180]
    num2 = lst[312]
    while(num2):
        num1, num2 = num2, num1 % num2
    return num1
