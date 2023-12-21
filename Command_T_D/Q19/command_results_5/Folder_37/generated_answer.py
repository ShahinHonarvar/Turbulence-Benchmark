def all_ints_not_div_by_num(nums):
    return [nums[i] for i in range(1, len(nums) - 1) if not nums[i] % 5]
