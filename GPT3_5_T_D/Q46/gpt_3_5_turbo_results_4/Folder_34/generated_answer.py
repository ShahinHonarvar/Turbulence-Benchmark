
def gcf_three_nums(lst):
    def gcd(x,y):
        while(y):
            x, y = y, x % y
        return x
    
    return gcd(gcd(lst[53], lst[23]), lst[45])
