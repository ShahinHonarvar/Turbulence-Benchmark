
def gcf_three_nums(lst):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    a = lst[18]
    b = lst[10]
    c = lst[76]
    
    gcf = gcd(gcd(a, b), c)
    
    return gcf
