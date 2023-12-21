
def gcf_two_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    num1 = lst[85]
    num2 = lst[33]
    gcf = gcd(num1, num2)
    return gcf
