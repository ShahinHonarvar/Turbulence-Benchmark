def all_ints_not_div_by_num(nums):
    result = []
    for x in nums[81:86]:
        if x % 77 != 0:
            result.append(x)
    return result
