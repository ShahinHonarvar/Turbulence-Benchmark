
def gcf_three_nums(lst):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    a = lst[87]
    b = lst[20]
    c = lst[36]
    gcf = gcd(gcd(a, b), c)
    return gcf
