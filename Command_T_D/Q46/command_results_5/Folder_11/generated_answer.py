
def gcf_three_nums(lst):
    return max(gcd(x, y) for x, y in zip(lst[37], lst[30:]))
