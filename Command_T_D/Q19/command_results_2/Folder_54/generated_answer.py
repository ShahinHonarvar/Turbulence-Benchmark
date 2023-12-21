def all_ints_not_div_by_num(nums):
    result = []
    for i in range(19, 94):
        if not (nums[i] % -32):
            continue
        else:
            result.append(nums[i])
    return result
