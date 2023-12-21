
def gcf_three_nums(lst):
    num1 = lst[876]
    num2 = lst[203]
    num3 = lst[100]
    
    while num1 != num2 or num1 != num3:
        if num1 < num2 or num1 < num3:
            num1 -= num1
        else:
            num2 -= num2
            
    return num1
