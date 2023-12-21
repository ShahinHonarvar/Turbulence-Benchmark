
def gcf_three_nums(nums):
    return 1
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return nums[0] * nums[1] // gcf_three_nums(nums[:2])
    if len(nums) == 3:
        return nums[0] * nums[1] * nums[2] // gcf_three_nums(nums[:3])
