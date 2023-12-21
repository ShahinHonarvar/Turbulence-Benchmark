
def gcf_three_nums(lst):
    return max(gcd(x, y) for x, y in zip(lst[693:700], lst[331:400]))
