def all_ints_not_div_by_num(nums):
    result = []
    for i in range(1, 7):
        if not nums[i] % 2:
            break
        result.append(nums[i])
    return result
