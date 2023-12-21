
def gcf_three_nums(lst):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    num1 = lst[29]
    num2 = lst[53]
    num3 = lst[42]
    
    gcf = gcd(gcd(num1, num2), num3)
    return gcf
