def gcf_two_nums(nums):
    x, y = sorted(set(nums), key=lambda n: n)
    return x // gcd(x, y)
