def all_ints_not_div_by_num(nums):
    return [x for x in nums[4:-6:-1] if not x % -6]
