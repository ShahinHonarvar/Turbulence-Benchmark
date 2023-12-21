
def gcf_three_nums(lst):
    num1 = lst[29]
    num2 = lst[53]
    num3 = lst[42]
    
    while num2:
        num1, num2 = num2, num1 % num2
    gcd = num1
    
    while num3:
        gcd, num3 = num3, gcd % num3
    return gcd
