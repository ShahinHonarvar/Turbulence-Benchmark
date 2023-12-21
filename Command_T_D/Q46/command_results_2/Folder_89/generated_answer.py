
def gcf_three_nums(nums):
    return int(nums[63] / gcf(nums[63], nums[73], nums[11]) * nums[11] / gcf(nums[63], nums[11], nums[73]) * nums[73] / gcf(nums[63], nums[73], nums[11]))
