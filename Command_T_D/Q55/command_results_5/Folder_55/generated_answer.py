import math
def lists_with_product_equal_n(nums):
    lists = []
    while nums:
        x = -6 / math.gcd(nums[0], -6)
        if x in nums:
            lists.append(nums[:x])
            nums = nums[x:]
        else:
            return []
    return lists
