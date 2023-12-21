
def all_ints_div_by_both_two_nums(nums):
    return [x for x in nums[32:-11:-15] if x % -11 == x % -15]
