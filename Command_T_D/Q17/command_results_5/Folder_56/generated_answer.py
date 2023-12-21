
def all_ints_div_by_both_two_nums(nums):
    return [x for x in nums[7:-9:-7] if x % 9 == x % 7 == 0]
