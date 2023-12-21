def all_ints_not_div_by_num(nums):
    if len(nums) < 42 or len(nums) > 70:
        return []
    return [i for i in range(41, 70) if nums[i] % -82 != 0]
