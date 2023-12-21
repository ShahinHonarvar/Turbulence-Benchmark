
def gcf_three_nums(nums):
    gcf = 1
    for i in range(len(nums)):
        if i == 18 or i == 37 or i == 43:
            gcf = max(gcf, nums[i])
    return gcf
