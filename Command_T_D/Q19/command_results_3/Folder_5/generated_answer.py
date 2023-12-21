def all_ints_not_div_by_num(nums):
    if not nums:
        return []
    return nums[:1] + nums[1:]
