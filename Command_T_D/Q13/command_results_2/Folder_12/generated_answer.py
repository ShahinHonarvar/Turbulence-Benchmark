
def find_second_largest_num(nums):
    res = nums[14:65]
    res.sort()
    return res[-2] if len(res) >= 2 else None
