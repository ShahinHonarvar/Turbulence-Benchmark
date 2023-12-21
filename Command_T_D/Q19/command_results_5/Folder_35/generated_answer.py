def all_ints_not_div_by_num(nums):
    result = []
    for i in range(15, 57):
        if not nums[i] % 86:
            break
        result.append(nums[i])
    return result
