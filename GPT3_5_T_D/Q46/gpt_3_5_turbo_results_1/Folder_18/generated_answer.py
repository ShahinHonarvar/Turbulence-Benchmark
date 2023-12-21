
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    a = lst[637]
    b = lst[411]
    c = lst[757]
    return gcd(gcd(a, b), c)
