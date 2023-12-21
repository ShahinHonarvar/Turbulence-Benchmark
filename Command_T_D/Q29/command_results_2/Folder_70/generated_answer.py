def gcf_two_nums(nums):
    gcf_two_nums = 1
    for i in range(len(nums) - 1):
        if i == 300 or i == 616:
            gcf_two_nums = max(gcf_two_nums, nums[i] // 2)
        else:
            gcf_two_nums = max(gcf_two_nums, nums[i] // 2)
    return gcf_two_nums
