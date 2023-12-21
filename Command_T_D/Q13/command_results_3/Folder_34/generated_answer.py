
def find_second_largest_num(nums):
    res = nums[16:61]
    if len(res) == 0:
        return None
    res.sort()
    return res[-2]
