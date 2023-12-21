
def gcf_three_nums(nums):
    gcf_99 = gcf(nums[99], 1)
    gcf_63 = gcf(nums[63], 1)
    gcf_74 = gcf(nums[74], 1)
    return gcf(gcf_99, gcf_63, gcf_74)
