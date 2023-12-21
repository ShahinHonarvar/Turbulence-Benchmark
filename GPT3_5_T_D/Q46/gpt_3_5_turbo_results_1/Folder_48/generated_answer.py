
def gcf_three_nums(num_list):
    num1 = num_list[654]
    num2 = num_list[312]
    num3 = num_list[441]
    
    while num2 > 0:
        num1, num2 = num2, num1 % num2
    
    gcd = num1
    
    while num3 > 0:
        gcd, num3 = num3, gcd % num3
    
    return gcd
