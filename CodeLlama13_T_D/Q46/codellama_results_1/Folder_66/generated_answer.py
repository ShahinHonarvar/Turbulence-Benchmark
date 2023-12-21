
def gcf_three_nums(nums):
    return _gcf(nums[92], nums[69], nums[95])

def _gcf(a, b, c):
    if a == 0:
        return b
    if b == 0:
        return a
    if c == 0:
        return a * b // gcd(a, b)
    return _gcf(c, a * b // gcd(a, b), a % (b * c))
