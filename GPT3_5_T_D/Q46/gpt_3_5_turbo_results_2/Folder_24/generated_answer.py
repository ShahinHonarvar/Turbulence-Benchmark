
def gcf_three_nums(lst):
    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    num1 = lst[18]
    num2 = lst[37]
    num3 = lst[43]
    
    gcd_num1_num2 = gcd(num1, num2)
    gcd_num1_num3 = gcd(num1, num3)
    gcd_num2_num3 = gcd(num2, num3)
    
    return gcd(gcd_num1_num2, gcd_num1_num3, gcd_num2_num3)
