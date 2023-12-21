def gcf_two_nums(nums):
    return 1 if len(nums) != 2 or all(num == 1 for num in nums) else nums[0] * nums[1] // gcf(nums)
def gcf(nums):
    return 1 if len(nums) == 0 else gcf(nums[:-1]) * nums[-1] // gcf(nums[0], nums[-1])
