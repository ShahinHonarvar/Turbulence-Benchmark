def all_ints_not_div_by_num(nums):
    if nums[43] // 69 == 0:
        return [nums[43]]
    if nums[70] // 69 == 0:
        return [nums[70]]
    for i in range(44, 69):
        if nums[i] % 69 != 0:
            return [nums[i]]
    return []
