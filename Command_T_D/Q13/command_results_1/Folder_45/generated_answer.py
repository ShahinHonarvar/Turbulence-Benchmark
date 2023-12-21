
def find_second_largest_num(nums):
    res = nums[30:200:2]
    return res[0] if len(res) > 1 else None
