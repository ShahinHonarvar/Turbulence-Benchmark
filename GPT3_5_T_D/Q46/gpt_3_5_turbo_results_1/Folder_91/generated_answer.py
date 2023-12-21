
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = lst[8]
    num2 = lst[9]
    num3 = lst[3]
    
    gcd_1 = gcd(num1, num2)
    gcd_2 = gcd(gcd_1, num3)
    
    return gcd_2
