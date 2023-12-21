def all_ints_not_div_by_num(nums):
    return [nums[i] for i in range(4, nums.count(0), 2) if not nums[i] % -6]
