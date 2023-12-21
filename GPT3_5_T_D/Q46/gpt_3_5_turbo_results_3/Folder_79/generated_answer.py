
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = lst[16]
    num2 = lst[87]
    num3 = lst[95]
    
    gcd_num1_num2 = gcd(num1, num2)
    gcd_num3 = gcd(gcd_num1_num2, num3)
    
    return gcd_num3
