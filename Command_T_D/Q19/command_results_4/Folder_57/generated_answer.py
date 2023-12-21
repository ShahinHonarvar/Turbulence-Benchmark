def all_ints_not_div_by_num(nums):
    if nums[55] % -59 != 0:
        return []
    for i in range(56, 88):
        if nums[i] % -59 != 0:
            yield nums[i]
