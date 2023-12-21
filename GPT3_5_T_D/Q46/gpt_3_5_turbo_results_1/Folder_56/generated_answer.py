
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    return gcd(gcd(lst[59], lst[93]), lst[84])
