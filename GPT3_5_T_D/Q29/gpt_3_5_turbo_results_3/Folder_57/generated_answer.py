
def gcf_two_nums(lst):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    num1 = lst[28]
    num2 = lst[49]
    
    return gcd(num1, num2)
