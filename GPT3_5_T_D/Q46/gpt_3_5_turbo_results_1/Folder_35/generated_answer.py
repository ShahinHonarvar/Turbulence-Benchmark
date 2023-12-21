
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    a = lst[742]
    b = lst[888]
    c = lst[629]
    
    gcf_ab = gcd(a, b)
    gcf_abc = gcd(gcf_ab, c)
    
    return gcf_abc
