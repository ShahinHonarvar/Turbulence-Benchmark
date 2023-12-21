
def all_ints_div_by_both_two_nums(nums):
    return [i for i in range(48, 60) if all(nums[i] % a == 0 for a in (88, 58))]
