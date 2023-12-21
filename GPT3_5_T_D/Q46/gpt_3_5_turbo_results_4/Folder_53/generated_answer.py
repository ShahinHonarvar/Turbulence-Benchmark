
def gcf_three_nums(lst):
    num1 = lst[66]
    num2 = lst[56]
    num3 = lst[92]
    
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    gcd = num1
    
    while num3 != 0:
        gcd, num3 = num3, gcd % num3
    
    return gcd
