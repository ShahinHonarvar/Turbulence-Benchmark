def all_ints_not_div_by_num(nums):
    res = [x for x in nums[13:76] if not (x % 44 == 0)]
    return res
