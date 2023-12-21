
def gcf_two_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    return gcd(lst[360], lst[722])
