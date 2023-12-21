def all_ints_not_div_by_num(nums):
    result = []
    for i in range(11, 56):
        if not nums[i] % 90:
            continue
        result.append(nums[i])
    return result
