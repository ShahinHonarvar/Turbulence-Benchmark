
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    return gcd(gcd(lst[0], lst[8]), lst[3])
