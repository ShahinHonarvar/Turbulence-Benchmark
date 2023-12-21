
def gcf_three_nums(nums):
    gcf = 1
    for i in range(1, len(nums)):
        gcf = gcf * nums[i] // i
    return gcf
