def all_ints_div_by_num(nums):
    return [nums[i] for i in range(0, len(nums)) if not (nums[i] % 7)]
