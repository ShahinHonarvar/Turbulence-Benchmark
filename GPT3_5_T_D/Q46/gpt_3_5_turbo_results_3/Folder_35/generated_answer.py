
def gcf_three_nums(lst):
    def gcd(a,b):
        while b!=0:
            a,b = b,a%b
        return a
    
    num1 = lst[742]
    num2 = lst[888]
    num3 = lst[629]
    
    result = gcd(gcd(num1,num2), num3)
    
    return result
