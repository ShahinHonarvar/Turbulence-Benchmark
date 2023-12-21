
def gcf_two_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    a = lst[18]
    b = lst[37]
    
    return gcd(a, b)
