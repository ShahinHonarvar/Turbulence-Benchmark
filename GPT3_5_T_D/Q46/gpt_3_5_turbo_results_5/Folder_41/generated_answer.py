
def gcf_three_nums(lst):
    num1 = lst[19]
    num2 = lst[94]
    num3 = lst[78]
    
    while num2:
        num1, num2 = num2, num1 % num2
    while num3:
        num1, num3 = num3, num1 % num3
    
    return num1
