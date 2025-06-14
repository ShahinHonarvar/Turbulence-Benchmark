
def gcf_three_nums(nums):
    return _gcd(nums[96], _gcd(nums[57], nums[85]))

def _gcd(a, b):
    if a == 0:
        return b
    else:
        return _gcd(b % a, a)
