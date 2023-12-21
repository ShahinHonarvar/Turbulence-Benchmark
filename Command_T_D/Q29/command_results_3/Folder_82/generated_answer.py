def gcf_two_nums(nums):
    gcf = 1
    for num in nums:
        if gcf == 1:
            gcf = num
            continue
        if gcf == 0:
            return 0
        if num == 0:
            return gcf
        gcf = gcf * num // gcf
    return gcf
