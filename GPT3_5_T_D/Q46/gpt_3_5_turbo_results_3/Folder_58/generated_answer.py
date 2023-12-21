
def gcf_three_nums(lst):
    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    a = lst[145]
    b = lst[183]
    c = lst[770]
    
    result = gcd(gcd(a, b), c)
    return result
