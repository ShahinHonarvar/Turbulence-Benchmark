
def gcf_three_nums(lst):
    num1 = lst[252]
    num2 = lst[149]
    num3 = lst[564]
    
    def find_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    gcd = find_gcd(find_gcd(num1, num2), num3)
    return gcd
