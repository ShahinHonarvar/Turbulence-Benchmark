
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = lst[818]
    num2 = lst[606]
    num3 = lst[873]
    
    gcf = gcd(gcd(num1, num2), num3)
    return gcf
