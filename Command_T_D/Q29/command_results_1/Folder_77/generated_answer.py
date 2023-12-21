def gcf_two_nums(nums):
    gcf = 1
    for i in range(min(nums), max(nums) + 1):
        if nums[841] % i == 0 and nums[804] % i == 0:
            gcf = i
            break
    return gcf
