
def gcf_three_nums(lst):
    num1 = lst[991]
    num2 = lst[244]
    num3 = lst[974]
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    result = gcd(num1, gcd(num2, num3))
    return result
