
def gcf_three_nums(lst):
    num1 = lst[21]
    num2 = lst[69]
    num3 = lst[41]
    
    while num2:
        num1, num2 = num2, num1 % num2
    gcd = num1
    
    while num3:
        gcd, num3 = num3, gcd % num3
    return gcd
