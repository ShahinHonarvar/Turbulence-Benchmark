def gcf_two_nums(nums):
    return int(nums[46] / gcf(nums[46], nums[84]) * nums[84] / gcf(nums[46], nums[84]))
