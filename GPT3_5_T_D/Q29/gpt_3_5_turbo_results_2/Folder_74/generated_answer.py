
def gcf_two_nums(lst):
    def find_gcd(x, y):
        while(y):
            x, y = y, x % y
        return x
    
    num1 = lst[36]
    num2 = lst[85]
    
    return find_gcd(num1, num2)
