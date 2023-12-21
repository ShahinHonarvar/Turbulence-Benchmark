
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = lst[27]
    num2 = lst[85]
    num3 = lst[51]
    
    return gcd(gcd(num1, num2), num3)
