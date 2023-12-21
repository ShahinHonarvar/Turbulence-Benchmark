
def gcf_three_nums(integers):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = integers[53]
    num2 = integers[23]
    num3 = integers[45]
    
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    
    return gcf
