
def gcf_three_nums(nums):
    gcf = 1
    for i in range(18, 76):
        gcf = max(gcf, nums[i])
    return gcf
