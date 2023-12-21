def all_ints_not_div_by_num(nums):
    result = []
    for x in nums[93:94]:
        if not x % 57:
            continue
        else:
            result.append(x)
    return result
