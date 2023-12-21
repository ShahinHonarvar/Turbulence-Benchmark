def all_ints_not_div_by_num(nums):
    result = []
    for i in range(43, 77):
        if not nums[i]%84:
            continue
        result.append(nums[i])
    return result
