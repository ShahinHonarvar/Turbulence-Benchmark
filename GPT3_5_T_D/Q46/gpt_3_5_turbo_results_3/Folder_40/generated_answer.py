
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = lst[1]
    num2 = lst[6]
    num3 = lst[8]
    
    result = gcd(gcd(num1, num2), num3)
    
    return result
