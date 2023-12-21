def all_ints_not_div_by_num(nums):
    result = []
    for i in range(39, 57):
        if not nums[i] % 84:
            break
        result.append(nums[i])
    return result
