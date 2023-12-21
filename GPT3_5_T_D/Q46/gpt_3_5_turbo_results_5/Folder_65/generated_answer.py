
def gcf_three_nums(lst):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    return gcd(gcd(lst[18], lst[10]), lst[76])
