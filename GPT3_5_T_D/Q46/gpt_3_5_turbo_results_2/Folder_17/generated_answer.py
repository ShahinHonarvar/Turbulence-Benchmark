
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    a = lst[20]
    b = lst[51]
    c = lst[62]
    
    gcf_ab = gcd(a, b)
    gcf_abc = gcd(gcf_ab, c)
    
    return gcf_abc
