
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = lst[25]
    num2 = lst[76]
    num3 = lst[57]
    
    gcf = gcd(num1, gcd(num2, num3))
    
    return gcf
