
def gcf_two_nums(lst):
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    
    num1 = lst[166]
    num2 = lst[106]
    
    return gcd(num1, num2)
