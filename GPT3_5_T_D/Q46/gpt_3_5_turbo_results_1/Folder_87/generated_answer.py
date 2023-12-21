
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    num1 = lst[74]
    num2 = lst[60]
    num3 = lst[28]
    
    gcf1 = gcd(num1, num2)
    gcf_result = gcd(gcf1, num3)
    
    return gcf_result
