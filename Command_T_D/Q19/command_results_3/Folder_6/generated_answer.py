def all_ints_not_div_by_num(nums):
    result = []
    for i in range(43, 70):
        if not nums[i] % 69:
            break
        result.append(nums[i])
    return result
