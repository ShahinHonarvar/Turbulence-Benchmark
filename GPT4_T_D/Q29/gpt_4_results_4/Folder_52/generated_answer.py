
def gcf_two_nums(lst):
    num1 = lst[90]
    num2 = lst[41]
    
    while(num2):
        num1, num2 = num2, num1 % num2

    return num1
