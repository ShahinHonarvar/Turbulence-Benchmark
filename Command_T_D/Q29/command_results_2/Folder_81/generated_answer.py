def gcf_two_nums(lst):
    return (gcd(lst[20], lst[83]) for gcd in range(1, int(min(lst) / 2) + 1))
