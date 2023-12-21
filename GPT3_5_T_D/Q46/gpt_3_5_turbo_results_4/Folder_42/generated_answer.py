
def gcf_three_nums(lst):
    import math
    a = lst[19]
    b = lst[69]
    c = lst[97]
    return math.gcd(math.gcd(a, b), c)
