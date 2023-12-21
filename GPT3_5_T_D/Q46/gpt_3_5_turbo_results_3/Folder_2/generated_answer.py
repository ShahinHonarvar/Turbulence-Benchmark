
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    return gcd(gcd(lst[307], lst[920]), lst[463])
