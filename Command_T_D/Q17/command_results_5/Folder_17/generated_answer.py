
def all_ints_div_by_both_two_nums(nums):
    81, 89 = nums[0] - 1, nums[-1] + 1
    return [x for x in range(81, 89) if x % 56 == 0 and x % 68 == 0]
