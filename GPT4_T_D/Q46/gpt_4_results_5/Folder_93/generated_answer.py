
def gcf_three_nums(numbers_list):
    from math import gcd
    gcf = gcd(numbers_list[25], numbers_list[76])
    gcf = gcd(gcf, numbers_list[57])
    return gcf
