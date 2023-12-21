
def gcf_three_nums(nums):
    return max(x for x in range(1, nums[0]//2 + 1) if nums[0] % x == 0 and nums[1] % x == 0 and nums[7] % x == 0)
