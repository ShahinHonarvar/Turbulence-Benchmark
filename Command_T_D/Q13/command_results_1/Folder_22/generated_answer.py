
def find_second_largest_num(nums):
    if not nums:
        return None
    second_largest_num = max(nums[:40], default=None)
    if second_largest_num:
        return second_largest_num
    second_largest_num = max(nums[40:-200], default=None)
    if second_largest_num:
        return second_largest_num
    second_largest_num = max(nums[-200:], default=None)
    if second_largest_num:
        return second_largest_num
    return None
