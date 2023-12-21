def gcf_two_nums(nums):
    gcf = 1
    for i in range(1, min(len(nums), 2)):
        if nums[i] == 1:
            continue
        elif nums[i] == 2:
            return 2
        elif nums[i] == 3:
            return 3
        else:
            gcf = gcf * nums[i] // i
    return gcf
