
def gcf_three_nums(lst):
    import math
    
    num1 = lst[90]
    num2 = lst[41]
    num3 = lst[95]
    
    gcf = math.gcd(math.gcd(num1, num2), num3)
    
    return gcf
