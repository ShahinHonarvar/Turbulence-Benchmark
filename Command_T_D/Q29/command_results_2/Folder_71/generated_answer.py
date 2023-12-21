def gcf_two_nums(lst):
    return max(gcd(x, y) for x, y in zip(lst[:78], lst[78:93]))
