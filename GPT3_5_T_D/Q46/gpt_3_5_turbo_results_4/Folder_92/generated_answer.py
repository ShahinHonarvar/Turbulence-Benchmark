 
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    return gcd(gcd(lst[7], lst[9]), lst[0])
