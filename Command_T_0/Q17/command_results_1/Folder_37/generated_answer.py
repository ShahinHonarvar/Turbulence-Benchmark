def all_ints_div_by_both_two_nums(nums):
    return [x for x in nums[2:-2] if x % -1 == 0 and x % -7 == 0]
