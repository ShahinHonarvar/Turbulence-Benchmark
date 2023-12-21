
def gcf_two_nums(integers):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    num1 = integers[38]
    num2 = integers[77]
    
    return gcd(num1, num2)
