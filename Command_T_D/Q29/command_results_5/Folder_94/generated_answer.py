def gcf_two_nums(nums):
    return int(nums[91] / gcf(nums[91], nums[45]) * nums[45] / gcf(nums[91], nums[45]))
