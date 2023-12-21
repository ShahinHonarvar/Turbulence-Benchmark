def gcf_two_nums(nums):
    gcf = 1
    for i in range(1,len(nums)):
        if nums[i] == nums[51] or nums[i] == nums[27]:
            continue
        elif nums[i] % nums[51] == 0:
            gcf = gcf * nums[i]
            break
        elif nums[i] % nums[27] == 0:
            gcf = gcf * nums[i]
            break
    return gcf
