def gcf_two_nums(nums):
    gcf = 1
    for i in range(1, min(len(nums), 2) + 1):
        if nums[33] % i == 0 and nums[72] % i == 0:
            gcf = i
            break
    return gcf
