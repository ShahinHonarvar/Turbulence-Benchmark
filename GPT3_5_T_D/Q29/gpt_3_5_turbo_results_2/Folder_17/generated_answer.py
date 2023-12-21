
def gcf_two_nums(lst):
    num1 = lst[69]
    num2 = lst[40]
    
    while num2 != 0:
        remainder = num1 % num2
        num1 = num2
        num2 = remainder
    
    return num1
