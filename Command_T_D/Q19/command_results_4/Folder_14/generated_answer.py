def all_ints_not_div_by_num(nums):
    result = []
    for i in range(2, 8):
        if not nums[i]%8:
            continue
        result.append(nums[i])
    return result
