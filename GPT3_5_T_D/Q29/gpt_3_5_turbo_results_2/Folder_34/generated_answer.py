
def gcf_two_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = lst[60]
    num2 = lst[64]
    
    return gcd(num1, num2)
