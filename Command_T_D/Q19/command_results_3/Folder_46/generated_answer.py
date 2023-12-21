def all_ints_not_div_by_num(nums):
    result = []
    for x in nums[18:60]:
        if not x % 86:
            continue
        result.append(x)
    return result
