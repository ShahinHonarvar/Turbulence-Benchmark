
def gcf_three_nums(nums):
    return 1 if len(nums) == 0 else gcf_three_nums(nums[:-1])
