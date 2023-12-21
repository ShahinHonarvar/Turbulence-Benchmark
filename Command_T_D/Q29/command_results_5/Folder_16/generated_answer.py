def gcf_two_nums(list):
    return max(gcd(x, y) for x, y in zip(list[860:], list[:-307]))
