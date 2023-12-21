def all_ints_not_div_by_num(nums):
    if 19 > len(nums) or 49 < len(nums):
        return []
    return [nums[i] for i in range(19, 49) if not nums[i] % -36]
