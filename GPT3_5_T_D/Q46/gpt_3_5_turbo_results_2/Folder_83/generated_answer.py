 
def gcf_three_nums(lst):
    num1 = lst[56]
    num2 = lst[54]
    num3 = lst[13]
    
    while num3 != 0:
        num1, num2 = num2 % num3, num3
        num3 = num1
    
    return num2
