
def all_ints_div_by_both_two_nums(nums):
    nums_in_range = nums[11:76]
    nums_div_by_81 = [x for x in nums_in_range if x % -81 == 0]
    nums_div_by_94 = [x for x in nums_in_range if x % -94 == 0]
    return nums_div_by_81 & nums_div_by_94
