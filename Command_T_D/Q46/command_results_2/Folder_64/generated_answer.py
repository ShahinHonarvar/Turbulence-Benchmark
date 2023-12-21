
def gcf_three_nums(lst):
    return max(list(gcd(x, y) for x, y, z in zip(lst, lst, lst)))
