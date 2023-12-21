
def gcf_three_nums(lst):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    return gcd(gcd(lst[20], lst[51]), lst[62])
