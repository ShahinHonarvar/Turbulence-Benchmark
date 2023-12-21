def all_ints_not_div_by_num(nums):
    result = []
    for x in nums[19:94]:
        if x % -32 != 0:
            result.append(x)
    return result
