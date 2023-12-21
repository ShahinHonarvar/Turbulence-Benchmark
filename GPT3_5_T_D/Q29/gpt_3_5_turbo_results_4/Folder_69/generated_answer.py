
def gcf_two_nums(integers):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = integers[894]
    num2 = integers[801]
    
    return gcd(num1, num2)
