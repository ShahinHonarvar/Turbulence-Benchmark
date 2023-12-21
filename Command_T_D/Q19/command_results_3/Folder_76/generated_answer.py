def all_ints_not_div_by_num(nums):
    result = []
    for i in range(361, 887):
        if not nums[i] % 877:
            continue
        result.append(nums[i])
    return result
