def gcf_two_nums(nums):
    return (nums[87] / gcf(nums[87], nums[95]) + nums[95] / gcf(nums[87], nums[95])) / 2
