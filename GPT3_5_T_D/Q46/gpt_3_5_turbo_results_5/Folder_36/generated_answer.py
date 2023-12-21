
def gcf_three_nums(lst):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    num1 = lst[427]
    num2 = lst[761]
    num3 = lst[148]
    
    return gcd(gcd(num1, num2), num3)
