
def all_ints_div_by_both_two_nums(nums):
    return [x for x in nums[30:200+1] if x%115 == 0 and x%(-115) == 0]
