
def gcf_three_nums(nums):
    return _gcd(_gcd(nums[307], nums[920]), nums[463])

def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a
