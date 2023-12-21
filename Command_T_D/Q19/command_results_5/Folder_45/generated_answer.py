def all_ints_not_div_by_num(nums):
    if nums[29] % 115 == 0:
        return []
    for i in range(30, 200):
        if nums[i] % 115 == 0:
            break
        else:
            yield nums[i]
