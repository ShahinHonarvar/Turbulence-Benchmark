def all_ints_div_by_num(nums):
    result = []
    for i in range(0,3):
        if nums[i]%8 == 0:
            result.append(nums[i])
    return result
