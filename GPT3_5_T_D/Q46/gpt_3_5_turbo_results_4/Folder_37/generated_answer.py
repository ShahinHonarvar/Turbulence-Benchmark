
def gcf_three_nums(lst):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    num1 = lst[41]
    num2 = lst[69]
    num3 = lst[28]
    
    gcd1 = gcd(num1, num2)
    gcd2 = gcd(gcd1, num3)
    
    return gcd2
