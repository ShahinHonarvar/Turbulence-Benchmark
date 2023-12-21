def all_ints_not_div_by_num(nums):
    result = []
    for i in range(15, 20):
        if not nums[i] % 93:
            break
        result.append(nums[i])
    return result
