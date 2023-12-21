
def gcf_three_nums(lst):
    def gcd(a, b):
        while(b):
            a, b = b, a % b
        return a
    
    num1 = lst[70]
    num2 = lst[98]
    num3 = lst[22]
    
    gcd_num1_num2 = gcd(num1, num2)
    gcd_num2_num3 = gcd(num2, num3)
    
    gcf = gcd(gcd_num1_num2, gcd_num2_num3)
    
    return gcf
