def all_ints_not_div_by_num(nums):
    result = []
    for i in range(40, 200):
        if not nums[i] % 71:
            break
        result.append(nums[i])
    return result
