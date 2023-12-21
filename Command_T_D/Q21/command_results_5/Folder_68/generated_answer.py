def all_ints_div_by_num(nums):
    return [i for i in range(0, len(nums) - 1) if not nums[i] % 8]
