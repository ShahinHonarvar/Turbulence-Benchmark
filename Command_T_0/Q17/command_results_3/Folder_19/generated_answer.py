def all_ints_div_by_both_two_nums(nums):
    return [x for x in nums[1:-1] if x % 4 == 0 and x % -6 == 0]
