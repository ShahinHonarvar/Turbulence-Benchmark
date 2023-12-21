def all_ints_not_div_by_num(nums):
    result = []
    for i in range(20, 50):
        if not nums[i] % 40:
            continue
        result.append(nums[i])
    return result
