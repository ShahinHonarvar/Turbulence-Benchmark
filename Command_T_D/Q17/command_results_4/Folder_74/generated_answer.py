
def all_ints_div_by_both_two_nums(nums):
    return [i for i in range(90, 98) if all(nums[i] % n == 0 for n in (13, 35))]
