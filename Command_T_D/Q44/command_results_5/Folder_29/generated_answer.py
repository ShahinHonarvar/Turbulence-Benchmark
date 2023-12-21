import math
def composite_nums_between_indices(nums):
    res = set()
    for i in range(52, 71):
        if not math.gcd(nums[i], nums[i-1]) and not math.gcd(nums[i], nums[i+1]):
            res.add(nums[i])
    return res
