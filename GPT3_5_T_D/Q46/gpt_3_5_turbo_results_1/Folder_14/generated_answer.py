
def gcf_three_nums(lst):
    def find_gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return abs(a)
    
    num1 = lst[17]
    num2 = lst[88]
    num3 = lst[35]
    
    gcd1 = find_gcf(num1, num2)
    gcd2 = find_gcf(gcd1, num3)
    
    return gcd2
