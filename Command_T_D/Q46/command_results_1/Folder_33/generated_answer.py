
def gcf_three_nums(nums):
    return 1 if len(nums) == 0 else max(list(set(gcf(nums[252], nums[149], nums[564]) for gcf in range(1, max(nums) + 1) if gcf in nums)))
