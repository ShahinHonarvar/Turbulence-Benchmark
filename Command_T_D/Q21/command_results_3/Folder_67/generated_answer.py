def all_ints_div_by_num(nums):
    result = []
    for i in range(40, 68):
        if i % 16 == 0:
            result.append(nums[i])
    return result
