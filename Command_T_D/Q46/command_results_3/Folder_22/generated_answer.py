
def gcf_three_nums(nums):
    gcf = 1
    for i in range(27, 85, 51):
        if nums[i] != 0:
            gcf = gcf * nums[i]
            nums[i] = 0
    return gcf
