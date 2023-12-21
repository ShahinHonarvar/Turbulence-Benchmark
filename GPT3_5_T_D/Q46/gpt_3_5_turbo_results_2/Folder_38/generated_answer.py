
def gcf_three_nums(lst):
    num1 = lst[14]
    num2 = lst[21]
    num3 = lst[17]
    
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    
    while num3 != 0:
        num1, num3 = num3, num1 % num3
        
    return num1
