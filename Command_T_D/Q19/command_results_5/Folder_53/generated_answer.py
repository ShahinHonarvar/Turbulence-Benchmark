def all_ints_not_div_by_num(nums):
    if nums[199] % 200 == 0 or nums[200] % 200 == 0:
        return []
    return nums[199:201]
