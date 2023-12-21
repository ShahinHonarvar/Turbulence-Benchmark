
def gcf_three_nums(nums):
    gcf_list = [nums[404], nums[834], nums[517]]
    return max(gcf(nums) for nums in gcf_list)
