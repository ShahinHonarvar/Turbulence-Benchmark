def all_ints_div_by_num(nums):
    result = []
    for i in range(43, 77):
        if i % 14 == 0:
            result.append(nums[i])
    return result
