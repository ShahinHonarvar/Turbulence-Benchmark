
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    return gcd(gcd(lst[96], lst[57]), lst[85])
