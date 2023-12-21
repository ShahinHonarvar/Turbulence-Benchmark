
def gcf_three_nums(nums):
    gcf_87, gcf_20, gcf_36 = nums[87] // nums[87], nums[20] // nums[20], nums[36] // nums[36]
    return max(gcf_87, gcf_20, gcf_36)
